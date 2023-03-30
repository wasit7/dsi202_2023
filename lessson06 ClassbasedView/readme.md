# create book app
1. create project

```bash
$django-admin startproject myproject
$cd myproject/
```

2. create sale

```bash
$python manage.py startapp sale
```

register app in settings.py
```python
#settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sale',
```
3. create model
model Product

