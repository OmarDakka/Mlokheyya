from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib import messages
from django.db import IntegrityError
import bcrypt


def index(request):
    return render(request, "login.html")


def registration(request):
    if request.method == "POST":
        errors = models.User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        if request.POST['password'] != request.POST['confirmPassword']:
            return redirect("/")
        else:

            try:
                password = request.POST["password"]
                pw_hash = bcrypt.hashpw(
                    password.encode(), bcrypt.gensalt()).decode()
                user = models.create_users(
                    request.POST['fname'], request.POST['lname'], request.POST['email'], pw_hash, request.POST['birthday'])
            except IntegrityError as uniquefailed:
                errors["unique"] = "Email already exists, please use another email!"
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
            else:
                messages.success(request, "Successfully registered (or logged in)")
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return redirect("/welcome")

    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')


def login(request):
    if request.method == "POST":
        user = models.get_user(request.POST['email'])
        errors = models.User.objects.login_validator(request.POST)
        if user is None:
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect("/")
        if user:
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect("/")
            else:
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return redirect("/welcome")


def welcome(request):
    if 'id' in request.session:
        return redirect("/books")
    else:
        return redirect("/")