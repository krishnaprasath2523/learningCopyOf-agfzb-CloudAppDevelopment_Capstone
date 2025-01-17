from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

from django.urls import reverse

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    # If the request method is GET
    if request.method == 'GET':
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    # If the request method is GET
    if request.method == 'GET':
        return render(request, 'djangoapp/contact.html', context)



# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # handle the post request
    if request.method == 'POST':
        # Get username & password from the dictionary (request.POST)
        username = request.POST['username']
        password = request.POST['psw']

        # check if the provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # perform the user login operation
            login(request, user)
            # return HttpResponseRedirect('/djangoapp/')
            return redirect("/djangoapp/")
        else:
            # If not, return to login/registration page again
            return render(request, 'djangoapp/registration.html', context)
    else:
        return render(request, 'djangoapp/registration.html', context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('/djangoapp/')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        user_exist = False
        username = request.POST['username']
        password = request.POST['psw']
        logger.info(request.POST)
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        try:
            # check the user already exist or not
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        
        if not user_exist:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            # perform the user login operation
            login(request, user)
            return redirect("/djangoapp/")
        else:
            # If not, return to login page again
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

