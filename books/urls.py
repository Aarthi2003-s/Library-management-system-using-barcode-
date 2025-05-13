# books/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('edit/<str:access_no>/', views.edit_book, name='edit_book'),
    path('delete/<str:access_no>/', views.delete_book, name='delete_book'),
    path('list/', views.book_list, name='book_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
