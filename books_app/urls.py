from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('user_page/<int:user_id>',views.user_page),
    path('add_book',views.add_book),
    path('book/<int:book_id>', views.book),
    path('category/<int:category_id>',views.category),
    path('about_us',views.about_us),
<<<<<<< HEAD
    path('update_book/<int:book_id>',views.update_book_data),
    path('buy_book/<int:book_id>',views.buy_book),
    path('/books/exchange_book/<int:book_id>',views.exchange_book),
=======
    path('category/sort/<int:category_id>', views.sort),
>>>>>>> eff554dd2bd4c1e1cf914508beae63883ddf3ed0

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)