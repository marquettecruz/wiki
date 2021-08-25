from re import T
from django.http.response import HttpResponse
from encyclopedia import util
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
import random
import markdown2 as md

import encyclopedia


# Takes you to the index page and returns a list of all entries
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()

    })

# Shows a specific entry. takes an entry title and returns a title and the entry text formated from markdown to html
def showEntry(request, title):
        if(title in util.list_entries()):
            entryText = util.get_entry(title)
            return render(request, "encyclopedia/showEntry.html", {
            "title": title,
            "entry": md.markdown(entryText)})
        else:
            return index(request)
   
    

# Search entry by recieved by get method. If the entry doesnt exists returns a list of similar titles.
def searchEntry(request):
       if request.method == "GET":
            #Get the content of the searchTitle parameter
            title = request.GET["searchTitle"]
            #If the title exists in the list of entries show the entry
            print("search title is  " + title)
            entries = util.list_entries()
        
            if title in entries:
                return showEntry(request, title)
            else:
                likeEntries = []
                
                for i in range(0,len(entries)):
                  if title.lower() in entries[i].lower():
                     likeEntries.append(entries[i])
                return render(request, "encyclopedia/searchEntry.html", {
                     "likeEntries": likeEntries })
       else:
         return index(request)
   
#Adds a new entry
def addEntry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = "# " + title + "\n\n" +  request.POST["content"]
        entries = util.list_entries()
        if title not in entries and title!="":
            util.save_entry(title, content)
            return showEntry(request,title)
        else:
            return render(request, "The article already exists...")
    else:
        return render(request, "encyclopedia/newEntry.html")

#Displays entry that is going to be edited
def showEntryToEdit(request, title):
        entryText = util.get_entry(title)
        return render(request, "encyclopedia/editEntry.html", {
                     "title": title,
                     "entry": entryText })

#updates a specific entry
def updateEntry(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return showEntry(request, title)

# Returns a random entry
def randomEntry(request):
    print("inside randomEntry")
    entries = util.list_entries()
    print("length of entries list is ", len(entries))
    numberOfEntries = len(entries)
    
    #generates a random number between 0 and the entries lenght-1
    randEntry = random.randint(0,numberOfEntries-1)
    
    return showEntry(request, entries[randEntry])
