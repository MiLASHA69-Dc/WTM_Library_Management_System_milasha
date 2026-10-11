from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
            return redirect("home:index")
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid(): #check if this is a valid entry
            user = login_form.get_user() #cross check against users in my database
            login(request,user) #if valid entry, user in the databse, give perimission to login
            return redirect ('home:index')
    
    else:
        login_form = LoginForm()


    context = {
        'login_form':login_form
    }
    return render(request,"auth/login.html",context)


def registration_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect("accounts:login")

    else:
          registration_form = RegistrationForm()   

    context = {
        "register":registration_form
    }      

    return render(request,"auth/registration.html",context)

@login_required
def logout_view(request):
    logout(request)
    return redirect("accounts:login")