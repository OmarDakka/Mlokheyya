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
    path('category/sort/<int:category_id>', views.sort),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)