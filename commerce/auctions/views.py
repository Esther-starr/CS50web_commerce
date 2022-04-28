from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, create_listing


def index(request):
    return render(request, "auctions/index.html")


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


def createlisting(request):
    if request.method == "POST":
        #return render(request, "auctions/register.html")
        create_listing.objects.create(title = request.POST["title"], 
        description = request.POST["description"], 
        starting_bid= request.POST["starting_bid"],
        image = request.POST["image"],
        Category = request.POST["Category"]
        ) 
        
        return HttpResponseRedirect(reverse("index"))

        #create_listing.description.add(request.POST["description"])
        #create_listing.starting_bid.add(request.POST["starting_bid"])
        #create_listing.image.add(request.POST["image"])
        #create_listing.Category.add(request.POST["Category"])   
    else:
        return render(request, "auctions/create_listing.html")    

