from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product, Profile, Order, Item
from django.http import HttpResponse

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

def add_to_cart(request, product_id):
    # request.session['message'] = "hello "*10
    data = request.session.get('order_list',[])
    data.append(product_id)
    request.session['order_list']=data
    order={}
    for i in data:
        order[i] = order.get(i,0)+1
        
    d=[]
    for k,v in order.items():
       d.append({'product': k, 'quantity': v}) 
    request.session['order_table']=d
    return HttpResponse("product id: {} <br> order: {}".format(data,order))

from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from .models import Order, Item

class OrderCreateView(CreateView):
    model = Order
    fields = ['profile','reciept']
    template_name = 'order_form.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        d=[
                {'product': 1, 'quantity': 2},
                {'product': 2, 'quantity': 4},
                {'product': 3, 'quantity': 6},
            ]
        d=self.request.session['order_table']
        OrderItemFormSet = inlineformset_factory(Order, Item, fields=('product', 'quantity'), extra=len(d))
        if self.request.POST:
            data['orderitems'] = OrderItemFormSet(self.request.POST, instance=self.object)
        else:
            # Prefill Order form
            data['form'].initial = {'profile': self.request.user.profile}
            # Prefill Item inline formset
            # orderitem_initial = {'product': Product.objects.first(), 'quantity': 1}
            data['orderitems'] = OrderItemFormSet(instance=self.object, initial=d)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        self.object = form.save()
        if orderitems.is_valid():
            orderitems.instance = self.object
            orderitems.save()
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['profile'] = self.request.user.profile
        return initial


