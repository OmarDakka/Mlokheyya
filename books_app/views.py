from django.shortcuts import redirect, render
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


def book(request,book_id):
    context = {
        "book" : models.get_book_by_id(book_id)
    }
    return render (request,'book.html',context)

def user_page(request,user_id):
    context = {
        "user":get_user_by_id(user_id),
        'all_categories':models.get_all_categories()
    }
    return render (request,'user_page.html',context)

def add_book(request):
    title = request.POST['bookTitle']
    description = request.POST['bookDescription']
    location =  request.POST['location']
    book_category = models.Category.objects.get(id = request.POST['category'])
    price = request.POST['price']
    image = request.POST['addPicture']
    uploaded_by = get_user_by_id(request.session['id'])
    to_exchange_with = models.Category.objects.get(id = request.POST['to_exchange'])
    models.create_book(title,description,location,book_category,price,image,uploaded_by,to_exchange_with)
    return redirect(f"/books/user_page/{request.session['id']}")


def about_us(request):
    return render (request,'About_us.html')

