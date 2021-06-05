from django.http import request
from django.shortcuts import redirect, render
from . import models
from users_app.models import User, get_user_by_id

# Create your views here.
def index(request):
    context ={
        'all_categories':models.get_all_categories()
    }
    return render (request,'home.html',context)

def category(request, category_id):
    context = {
        'categories' : models.get_all_categories(),
        'books' : models.get_books(),
        'current_category' : models.get_category_by_id(category_id  ),
    }
    context['books'] = models.Book.objects.filter(book_category = context['current_category'])
    if request.method == 'POST':
        location = request.post['location']
        context['books'] = models.get_by_location(location)
        if request.POST['button'] == "a-z":
            context['books'] =  models.sort_a_z()
        if request.POST['button'] == "z-a":
            context['books'] =  models.sort_z_a()
        if request.POST['button'] == "price":
            context['books'] =  models.sort_a_z()

    return render (request,'Category.html', context)



def book(request,book_id):
    context = {
        "book" : models.get_book_by_id(book_id),
        "all_books":models.get_books(),
        "user":get_user_by_id(request.session['id']),
        'all_categories':models.get_all_categories(),

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

<<<<<<< HEAD
def update_book_data(request,book_id):
    title=request.POST['title']
    description=request.POST['description']
    location=request.POST['location']
    book_category = models.Category.objects.get(id = request.POST['category'])
    price=request.POST['price']
    to_exchange_with = models.Category.objects.get(id = request.POST['bookCategory'])
    models.update_book(book_id,title,description,location,book_category,price,to_exchange_with)
    return redirect(f'/books/book/{book_id}')

def buy_book(request,book_id):
    models.update_owner(book_id,request.session['id'])
    return redirect(f'/books/book/{book_id}')

def exchange_book(request,book_id):
    pass
=======
def sort(request,category_id):
    context = {
        'categories' : models.get_all_categories(),
        'books' : models.get_books(),
        'current_category' : models.get_category_by_id(category_id),
    }
    context['books'] = models.Book.objects.filter(book_category = models.get_category_by_id(category_id))
    if request.method == 'POST':
        location = request.POST['location']
        context['books'] = models.get_by_location(location)
        if request.POST['button'] == "a-z":
            context['books'] =  models.sort_a_z(category_id)
        if request.POST['button'] == "z-a":
            context['books'] =  models.sort_z_a(category_id)
        if request.POST['button'] == "price":
            context['books'] =  models.sort_a_z(category_id)
        
    return render(request,'Category.html', context)

>>>>>>> eff554dd2bd4c1e1cf914508beae63883ddf3ed0
