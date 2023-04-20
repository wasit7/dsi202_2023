from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product
from django.http import HttpResponse

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

def add_to_cart(request, product_id):
    # request.session['message'] = "hello "*10
    data = request.session.get('order',[])
    data.append(product_id)
    request.session['order']=data
    order={}
    for i in data:
        order_i=order.get(i,0)
        order_i=order_i+1
        order[i] = order_i
    request.session['table_order']=order
    return HttpResponse("product id: {} <br> order: {}".format(data,order))

def order_summary(request):
    context = {'table_order':request.session['table_order']}
    return render(request, 'order_summary.html', context=context)