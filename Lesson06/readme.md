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

add book_app to setting.py

```python
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_app',
]
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

# create function based API
1. create api app
2. create get_author fucntion
3. route url
4. run server to check results

# create class based API
1. book serializer
2. book class based views
3. route url
4. run server to check results
5. add serializer, views and url for author

# create html for front end
1. HTML template
2. Javascript