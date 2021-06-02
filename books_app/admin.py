from django.contrib import admin
from books_app.models import Book
from books_app.models import Comment
from books_app.models import Category
# Register your models here.

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Category)
