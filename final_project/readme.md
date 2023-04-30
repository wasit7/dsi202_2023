# Setup Project
## setup environment
```
$conda activate -n dsi202_2023
```

## create project
```
$django-admin startproject myproject
$cd myproject
```

## create apps
```
$python manage.py startapp myapp
$mkdir ./myapp/templates
mkdir ./myapp/sale
```
## insall apps
```python
#/myproject/settings.py
...
INSTALLED_APPS = [
    ...,
    'myapp',
    'sale',
    'django_extensions',
]
```

## create static and media folders
```
$mkdir ./media
$mkdir ./static
```

## config static and media
```python
#/myproject/settings.py
...
import os
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
```

## config urls
```python
#/myproject/urls.py
...
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sale/', include('sale.urls')),
    path('', include('myapp.urls'))
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
