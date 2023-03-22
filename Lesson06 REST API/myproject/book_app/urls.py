from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('api/books/', views.BookList.as_view()),
    path('api/books/<int:pk>/', views.BookDetail.as_view()),
    path('api/authors/', views.AuthorList.as_view()),
    path('api/authors/<int:pk>/', views.AuthorDetail.as_view()),
]