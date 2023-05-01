from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product, Profile, Order, Item
from django.http import HttpResponse
from .forms import OrderItemFormSet

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
       product = Product.objects.get(pk=k)
       unit_price = float(product.unit_price)
       d.append({'product': k, 'quantity': v, 'unit_price': unit_price, 'subtotal': v*unit_price}) 
    request.session['order_table']=d
    return HttpResponse("product id: {} <br> order: {} <br> d: {}".format(data,order,d))

from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory, ChoiceField

from .models import Order, Item
from django.contrib.auth.mixins import LoginRequiredMixin

class OrderCreateView(LoginRequiredMixin,CreateView):
    login_url = "login"
    model = Order
    fields = ['grand_total','reciept']
    template_name = 'order_form.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # d=[
        #         {'product': 1, 'quantity': 2},
        #         {'product': 2, 'quantity': 4},
        #         {'product': 3, 'quantity': 6},
        #     ]
        
        d=self.request.session.get('order_table',{})
        OrderItemFormSet = inlineformset_factory(
            Order,
            Item,
            fields=('id','product', 'quantity', 'unit_price', 'subtotal'),
            widgets={'quantity': ChoiceField(choices= [(i, str(i)) for i in range(1, 6)] ).widget},
            extra=len(d),
            can_delete=True,
        )
        if self.request.POST:
            data['orderitems'] = OrderItemFormSet(self.request.POST, instance=self.object)
        else:
            # data['form'].initial = {'profile': self.request.user.profile}
            data['orderitems'] = OrderItemFormSet(instance=self.object, initial=d)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        self.object = form.save(commit=False)
        self.object.profile = self.request.user.profile
        self.object.save()
        print(orderitems)
        if orderitems.is_valid():
            orderitems.instance = self.object
            orderitems.save()
            # self.request.session['order_table']={}
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['profile'] = self.request.user.profile
        return initial


from IPython.display import Image
import requests
import qrcode

def get_qr(mode="mobile", send_to="", amount=1.23):
    url='https://thq68saavk.execute-api.ap-southeast-1.amazonaws.com/api/thai_qr'
    r = requests.post(url, json={"mode":mode,"send_to":send_to, "amount":amount})
    code=r.json()['result']
    return code

from django.http import HttpResponse

def qr_image(request, amount):
    send_to='0987654321' #change to merchat's mobile promptpay
    code=get_qr(mode="mobile", send_to=send_to, amount= float(amount))
    print(code)
    img = qrcode.make(code,box_size=4)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response