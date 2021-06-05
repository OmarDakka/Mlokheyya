from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description','image','created_at','updated_at']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','book_category','price','uploaded_by','to_exchange_with','created_at','updated_at']