from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import *


def index(request):
    allTweets = Tweet.objects.all().order_by('-timestamp')
    
    paginator = Paginator(allTweets, 10)
    page_number = request.GET.get('page')
    POTP = paginator.get_page(page_number)
    return render(request, "network/index.html",{
        "allPosts":allTweets,
        "POTP":POTP
    })


@csrf_exempt
@login_required
def newPost(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    user = request.user
    data = json.loads(request.body)
    content = data.get("content","")
    newpost = Tweet(owner=user, content=content)
    newpost.save()
    
    return JsonResponse({"message": "Tweet sent successfully."}, status=201)


def profile(request,user_id):
    user = User.objects.get(pk=user_id)
    userPosts = Tweet.objects.filter(owner=user).order_by('-timestamp')
    following = Follow.objects.filter(following=user)
    follower = Follow.objects.filter(followers=user)
    
    try:
        c = follower.filter(following=User.objects.get(pk=request.user.id))
        if len(c) != 0:
            isFollow = True
        else:
            isFollow = False
    except:
        isFollow = False
    
    
    paginator = Paginator(userPosts, 10)
    page_number = request.GET.get('page')
    POTP = paginator.get_page(page_number)
    
    return render(request, "network/profile.html",{
        "userPosts":userPosts,
        "POTP":POTP,
        "following":following,
        "follower":follower,
        "isFollow": isFollow,
        "user_profile":user
    })


def follow(request):
    userfollow = request.POST['userfollow']
    currentUser = User.objects.get(pk=request.user.id)
    userfollowData = User.objects.get(username=userfollow)
    f = Follow(following=currentUser, followers=userfollowData)
    f.save()
    user_id = userfollowData.id
    return HttpResponseRedirect(reverse(profile, kwargs={'user_id':user_id}))


def following(request):
    currentUser = User.objects.get(pk=request.user.id)
    followingPeople = Follow.objects.filter(following=currentUser)
    allPosts = Tweet.objects.all().order_by('-timestamp')
    
    
    followingPosts = []
    
    for post in allPosts:
        for person in followingPeople:
            if person.followers == post.owner:
                followingPosts.append(post)
    
    paginator = Paginator(allPosts, 10)
    page_number = request.GET.get('page')
    POTP = paginator.get_page(page_number)
    
    return render(request, "network/following.html",{
        "POTP":POTP,
        "FilterPosts":followingPosts
    })


def unfollow(request):
    userfollow = request.POST['userfollow']
    currentUser = User.objects.get(pk=request.user.id)
    userfollowData = User.objects.get(username=userfollow)
    f = Follow.objects.get(following=currentUser, followers=userfollowData)
    f.delete()
    user_id = userfollowData.id
    return HttpResponseRedirect(reverse(profile, kwargs={'user_id':user_id}))


@csrf_exempt
@login_required
def edit(request,post_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        editPost = Tweet.objects.get(id=post_id)
        
        
        if data.get("content") is not None and data.get("switch") == "Edit":
            editPost.content = data["content"]
            editPost.save()
            return HttpResponse(status=204)
        if data.get("content") is not None and data.get("switch") == "Liked":
            userLiked = User.objects.get(pk=int(data.get("content")))
            if userLiked not in editPost.likes.all():
                editPost.likes.add(userLiked)
            else:
                editPost.likes.remove(userLiked)
                
            editPost.save()
            return HttpResponse(status=204)
    else:
        return HttpResponse(status=400)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
