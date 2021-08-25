from django.urls import path

from . import views

app_name = "entries"

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/newEntry", views.addEntry, name = "addEntry"),
    path("wiki/search", views.searchEntry, name = "search"),
    path("wiki/random", views.randomEntry, name = "random"),
    path("wiki/<str:title>", views.showEntry, name = "showEntry"),
    path("wiki/<str:title>/updated", views.updateEntry, name = "updateEntry"),
    path("wiki/<str:title>/editEntry", views.showEntryToEdit, name = "showEntryToEdit"),
    
    
 
    
    
    
   
    
]
