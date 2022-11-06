from django.shortcuts import render
from markdown2 import Markdown
from django import forms
import random
from . import util


class searchForm(forms.Form):
    search_bar= forms.CharField()
    
def convertor(title):
    page = util.get_entry(title)
    markdowner = Markdown()
    if page == None:
        return None
    else: 
        return markdowner.convert(page)
    

def index(request):
    searchBar = searchForm()
    return render(request, "encyclopedia/index.html", {
        
        "entries": util.list_entries(),
        "searchBar" : searchBar
    })

def entry(request, title):
    html = convertor(title)
    if html == None:
        return render(request, "encyclopedia/error.html",{
            "message" : "Error(404) page not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content" : html
        })
    
        
def search(request):
    # 1-check if method is post mean data to server
    if request.method == "POST":
        # If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
        bar = searchForm(request.POST)
        # 2- if search bar has data mean is valid then ....
        if bar.is_valid():
            # 3- get this data and store it
            bar_text = bar.cleaned_data["search_bar"]
            # 4- convert dm to html is search bar data not null or file is exsist.
            html = convertor(bar_text)
            if html is not None:
                return render(request, "encyclopedia/entry.html", {
                    "title" : bar_text,
                    "content" : html
                })
            
            else:
                # the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring
                text_bar = bar.cleaned_data["search_bar"]
                
                pages = util.list_entries()
                recom = []
                for page in pages:
                    if text_bar.lower() in page.lower():
                        recom.append(page)
                return render(request, "encyclopedia/search.html",{
                    "recom" : recom
                })
                
def newPage(request):
    
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        
        
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html",{
                "message" : "Error(403):Entry Page alradey Exists."
            })
        else:
            util.save_entry(title, content)
            html_content = convertor(title)
            return render(request, "encyclopedia/entry.html", {
                "title" : title,
                "content" : html_content
            })
            
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title":title,
            "content":content
        })
        
def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html = convertor(title)
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content": html
        })
        
def rand(request):
    all = util.list_entries()
    rand_entry = random.choice(all)
    html = convertor(rand_entry)
    return render(request, "encyclopedia/entry.html",{
        "title":rand_entry,
        "content": html
    })
        