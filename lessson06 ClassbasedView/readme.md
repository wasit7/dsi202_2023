# create book app
1. create project

```bash
$django-admin startproject myproject
$cd myproject/
```

2. create an app clled "sale"

```bash
$python manage.py startapp sale
```

3. register app in settings.py
```python
#/myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sale',
```
4. create Product model
```python
#/myproject/sale/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)
```
5. create Views
```python
#/myproject/sale/views.py
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
```
6. add templates


```html
<!-- /myproject/sale/templates/product_detail.html -->
<h1>{{ object.name }}</h1>
<p>{{ object.description }}</p>
<p>Price: {{ object.price }}</p>
```


```html
<!-- /myproject/sale/templates/product_list.html -->
<h1>Product List</h1>
<ul>
{% for product in object_list %}
<li>{{ product.pk }} {{ product.name }} - {{ product.price }}</li>
{% endfor %}
</ul>
```

7. add app urls.py
```python
#/myproject/sale/urls.py
from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
]

```

8. add project urls.py
```python
#/myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sale/', include('sale.urls'))
]
```

9. assignment add link to list view
please adding url link to list view so that customer can click on id of product list to open product detail
hint: add url tag <a> in product_list.html and use reverse url to get an url for product detail

The results should look like the following images
![list view](../../contents/list_view.png)
![detail view](../../contents/detail_view.png)



