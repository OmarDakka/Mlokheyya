from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('reg',views.registration),
    path('logout',views.logout),
    path('login',views.login),
    path('welcome',views.welcome),
]