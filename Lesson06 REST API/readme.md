# create book app
1. create project

```bash
$django-admin startproject myproject
$cd myproject/
```

2. create book_app

```bash
$python manage.py startapp book_app
```

3. create models
```python
#models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```
4. register admin
```python
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
```
5. migrations and create superuser
```bash
$python manage.py makemigrations
$python manage.py migrate
$python manage.py createsuperuser
```

6. run server to check the admin page
```bash
python manage.py runserver
```

go to http://127.0.0.1:8000/admin/ 

# create function based API
0. install django-rest-framework 
```bash
$pip install djangorestframework
```
1. create api app using this folder structure
```bash
./api
├── __init__.py
└── views.py
```
add app in settings
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_app',
    'rest_framework',
    'api',
]
```
2. create get_author fucntion
```python
#views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_data(request):
    data={'name':'David', 'age':22}
    return Response(data)

```
3. route url in app and project
```python
#myproject/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
]
```
```python
#myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
```
4. run server to check results
go to http://127.0.0.1:8000/api/

# create class based API
1. book serializer
```python
#/myproject/book_app/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
```
2. book class based views
```python
#/myproject/book_app/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```
3. route url
```python
#/mayproject/book_app/urls.py
from django.urls import path
from . import views
from book_app.views import BookList, BookDetail

urlpatterns = [
    path('', views.get_data),
    path('books/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
]
```
4. run server to check results
gp to  http://127.0.0.1:8000/api/books/
5. add serializer, views and url for author
check github https://github.com/wasit7/dsi202_2023

# create html for front end
1. HTML template
2. Javascript