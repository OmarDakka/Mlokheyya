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
    #image field


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    book_category = models.ManyToManyField(Category,related_name="category_books")
    price = models.IntegerField()
    #image field
    uploaded_by = models.ForeignKey(User,related_name="book_user",on_delete=CASCADE)
    to_exchange_with = models.ManyToManyField(Category,related_name="exchange_category")
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
    book = models.ForeignKey(Book, related_name="method", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_books():
    return Book.objects.all()

def get_book_by_id(book_id):
    return Book.objects.get(id=book_id)

