from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Author
from .forms import CreateAuthorForm



def author_view(request): # The actual response creates here and returns it to the browser
    title = "Author Application"
    #return HttpResponse("<h2>Hello! Welcome to the Author app in my Library Management System web app</h2>")

    display_all_authors = Author.objects.all().order_by("-id") # This will display all the authors in the database in descending order of their id
    return render (request,"author/display_author.html",{"all_authors":display_all_authors})


def create_author(request):
    if request.method == "POST":
        create_author_form = CreateAuthorForm(request.POST)
        
        if create_author_form.is_valid():
            create_author_form.save()
            return redirect("display_author") # calling url by name in urls.py            
    else:
            create_author_form = CreateAuthorForm() # See empty form upon visiting the create_author.html

    context = {
            "author_form":create_author_form
        }    
    return render(request,"author/create_author.html",context)
