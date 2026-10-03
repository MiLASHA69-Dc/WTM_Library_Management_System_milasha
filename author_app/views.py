from django.shortcuts import render
from django.http import HttpResponse

def author_view(request): # The actual response creates here and returns it to the browser
    title = "Author Application"
    #return HttpResponse("<h2>Hello! Welcome to the Author app in my Library Management System web app</h2>")
    return render (request,"author.html",{"title":title})
