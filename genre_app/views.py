from django.shortcuts import render,redirect
from .models import Genre
from .forms import CreateGenreForm

# Create your views here.

def view_genre(request):
    all_genre=Genre.objects.all()
    if request.method == "POST":
        create_genre_form=CreateGenreForm(request.POST)
        if create_genre_form.is_valid():
            create_genre_form.save()
            return redirect("all_genres") 
    else:
        create_genre_form=CreateGenreForm()


    context={
        "display_genres":all_genre,
        "create_genre":create_genre_form
    }

    return render(request,"genre/display_genre.html",context)

def update_genre(request,update_id):
    get_genre=Genre.objects.get(id=update_id)
    if request.method == "POST":
        update_form=CreateGenreForm(request.POST,instance=get_genre)
        if update_form.is_valid():
            update_form.save()
            return redirect("all_genres")
    else:
        update_form=CreateGenreForm(instance=get_genre)

    context={
        "update_form":update_form
    }

    return render(request,"genre/update_genre.html",context)

def delete_genere(request,delete_id):
    get_genere=Genre.objects.get(id=delete_id)
    get_genere.delete()
    return redirect("all_genres") 


