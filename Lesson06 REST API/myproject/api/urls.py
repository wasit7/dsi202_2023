# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.get_data),
# ]

from django.urls import path
from . import views
from book_app.views import BookList, BookDetail

urlpatterns = [
    path('', views.get_data),
    path('books/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
]