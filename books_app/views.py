from django.shortcuts import render
from . import models
from users_app.models import User, get_user_by_id

# Create your views here.
def index(request):
    context ={
        'all_categories':models.get_all_categories()
    }
    return render (request,'home.html',context)

def category(request,category_id):
    context = {
        "category":models.get_category_by_id(id=category_id)
    }
    return render (request,'Category.html',context)


def book(request):
    return render (request,'book.html')

def user_page(request,user_id):
    context = {
        "user":get_user_by_id(user_id)
    }
    return render (request,'user_page.html',context)



def about_us(request):
    return render (request,'About_us.html')

