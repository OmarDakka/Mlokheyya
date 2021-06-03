from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user_page',views.user_page),
    path('book', views.book),
    path('category',views.category),
    path('home',views.home)

]
