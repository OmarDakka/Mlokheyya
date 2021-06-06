from re import search
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('search',views.search),
    path('user_page/<int:user_id>',views.user_page),
    path('add_book',views.add_book),
    path('book/<int:book_id>', views.book),
    path('category/<int:category_id>',views.category),
    path('about_us',views.about_us),
    path('update_book/<int:book_id>',views.update_book_data),
    path('buy_book/<int:book_id>',views.buy_book),
    path('exchange_book/<int:book_id>',views.exchange_book),
    path('category/sort/<int:category_id>', views.sort),
    path('delete_book/<int:book_id>',views.delete_book),

]
