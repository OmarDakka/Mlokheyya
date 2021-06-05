from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from users_app.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/' , default="default.jpg")


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    book_category = models.ForeignKey(Category,related_name="book_cat", default=None ,on_delete=CASCADE)
    price = models.IntegerField(default=None)
    image = models.ImageField(upload_to='images/' , default="default.jpg")
    uploaded_by = models.ForeignKey(User,related_name="book_user",on_delete=CASCADE)
    to_exchange_with = models.ForeignKey(Category,related_name="exchange_category", default=None ,on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField()
    book_comment = models.ForeignKey(Book,related_name="comment_on_book",on_delete=CASCADE)
    user_comment = models.ForeignKey(User,related_name="comment_by_user",on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Selling_method(models.Model):
    method = models.CharField(max_length = 255)
    book = models.ManyToManyField(Book, related_name="method")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    return Book.objects.get(id=book_id)

def get_all_categories():
    return Category.objects.all()

def get_category_by_id(id):
    return Category.objects.get(id=id)

def create_book(title,description,location,book_category,price,image,uploaded_by,to_exchange_with):
    new_book = Book.objects.create(title=title,description=description,location=location,book_category=book_category,price=price,image=image,uploaded_by=uploaded_by,to_exchange_with=to_exchange_with)
    return new_book

<<<<<<< HEAD
def update_book(book_id,title,description,location,book_category,price,to_exchange_with): 
    this_book = get_book_by_id(book_id)
    this_book.title=title 
    this_book.description=description
    this_book.location=location
    this_book.book_category=book_category
    this_book.price=price
    this_book.to_exchange_with=to_exchange_with
    this_book.save()
    return this_book

def update_owner(book_id,user_id):
    this_book = get_book_by_id(book_id)
    this_book.uploaded_by = User.objects.get(id=user_id)
    this_book.save()
    return this_book


=======

def get_by_location(location):
    return Book.objects.filter(location = location)


def sort_a_z(category_id):
    test= Category.objects.get(id=category_id)
    return test.book_cat.all().order_by('title')

def sort_z_a(category_id):
    test= Category.objects.get(id=category_id)
    return test.book_cat.all().order_by('-title')

def sort_price(category_id):
    test= Category.objects.get(id=category_id)
    return test.book_cat.all().order_by('price')
>>>>>>> eff554dd2bd4c1e1cf914508beae63883ddf3ed0


