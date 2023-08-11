from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Feature
# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render(request, "index.html", {"features":features})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["password2"]

        if password == confirm_password:
            user_email =User.objects.filter(email=email).exists()
            user_name =User.objects.filter(username=username).exists()
            if user_email:
                messages.info(request, "Email already exists")

            elif user_name:
                messages.info(request, "Email already exists")

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("login")
        else:
             return redirect("register")
    else:
        return render(request, "register.html")
    
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "user doees not exist kindly signup")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("index")

def counter(request):

    words = request.POST.get('words')
    amount_of_words= len(words.split())
    return render(request, "counter.html", {"amount":amount_of_words})
