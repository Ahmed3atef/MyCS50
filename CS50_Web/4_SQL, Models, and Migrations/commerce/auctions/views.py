from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    categories = Categories.objects.all()
    if request.method == "POST":
        try:
            category_id = Categories.objects.get(category=request.POST["category"])
            filterd = Listing.objects.filter(category=category_id.id)
            return render(request, "auctions/index.html",{
                "items":filterd,
                "categoryies":categories,
            })
        except Exception:
            return render(request, "auctions/index.html",{"message": "NO Items","categoryies":categories,})
    else:
        all_listing = Listing.objects.all()
        return render(request, "auctions/index.html",{
            "items":all_listing,
            "categoryies":categories,
            })

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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def createListing(request):
    if request.method == "POST":
        title = request.POST['itemName']
        imageUrl = request.POST['imageUrl']
        price = float(request.POST['price'])
        description = request.POST['description']
        category = Categories.objects.get(category=request.POST['category'])
        current_user = request.user

        b = Bids(price=price,user=current_user)
        b.save()
        l = Listing(title=title, description=description,image_url= imageUrl,bid=b,category=category, user=current_user)
        l.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "auctions/listingForm.html",{
            "categories":Categories.objects.all(),
            "edit":False,
        })

@login_required
def editListing(request,id):
    listing_item = Listing.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['itemName']
        imageUrl = request.POST['imageUrl']
        price = float(request.POST['price'])
        description = request.POST['description']
        category = Categories.objects.get(category=request.POST['category'])
        current_user = request.user
        ub = Bids.objects.get(user=current_user)
        ub.price = price
        ub.save()
        ub.price = price
        listing_item.title, listing_item.description, listing_item.image_url, listing_item.bid, listing_item.category = title, description, imageUrl, ub, category
        listing_item.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/listingForm.html",{
            "categories":Categories.objects.all(),
            "edit":True,
            "item":listing_item,
        })

def productView(request, id):
    product_view = Listing.objects.get(id=id)
    current_id = request.user
    inWatchlist = False if current_id in product_view.watchlist.all() else True
    comments = Comments.objects.filter(listing_comment = product_view)
    return render(request, "auctions/productView.html",{
        "product":product_view,
        "user":current_id,
        "inWatchlist":inWatchlist,
        "comments": comments,
        "bidUpdate": False
    })

def watchlistSwitch(request,id, switch):
    if switch == 0:
        watchlist = Listing.objects.get(id=id)
        watchlist.watchlist.add(request.user)
        return HttpResponseRedirect(reverse("productView", args=[watchlist.id]))
    elif switch == 1:
        watchlist = Listing.objects.get(id=id)
        watchlist.watchlist.remove(request.user)
        return HttpResponseRedirect(reverse("productView", args=[watchlist.id]))
    else:
        return HttpResponseRedirect(reverse("index"))

def watchlistView(request):
    categories = Categories.objects.all()
    current_user = request.user
    all_listing = current_user.watchlist.all()
    return render(request, "auctions/watchlist.html",{
    "items":all_listing,
    "categoryies":categories,
    })

def addComment(request, id):
    current_user = request.user
    listing = Listing.objects.get(pk=id)
    comment = request.POST['comment']
    newComment = Comments(author=current_user, listing_comment=listing, message=comment)
    newComment.save()
    return HttpResponseRedirect(reverse("productView", args=[listing.id]))

def addBids(request, id):
    current_user = request.user
    listing = Listing.objects.get(pk=id)
    bid = float(request.POST['bid'])
    inWatchlist = False if current_user in listing.watchlist.all() else True
    comments = Comments.objects.all()
    if listing.is_Active:
        if bid > listing.bid.price:
            ub = Bids(price=bid,user=current_user)
            ub.save()
            listing.bid = ub
            listing.save()
            return render(request, "auctions/productView.html",{
                "product":listing,
                "user":current_user,
                "inWatchlist":inWatchlist,
                "comments": comments,
                "updated":True,
                "bidUpdate": True
            })
        else:
            return render(request, "auctions/productView.html",{
                "product":listing,
                "user":current_user,
                "inWatchlist":inWatchlist,
                "comments": comments,
                "updated": False,
                "bidUpdate": True
            })
    else:
        return HttpResponseRedirect(reverse("index"))

def close(request, id):
    listing = Listing.objects.get(pk=id)
    listing.is_Active = False
    listing.save()
    return HttpResponseRedirect(reverse("index"))