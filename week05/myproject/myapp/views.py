#views.py
from django.http.response import HttpResponseRedirect 
from django.shortcuts import render, redirect
from .forms import ContactForm 
from django.http import HttpResponse

def home(request):
    return HttpResponse("""Hello, World!<br> Please contact us click <a href="contact">here</a>""")

def contact_us_view(request): 
   if request.method == "POST": 
       form = ContactForm(request.POST) 
       if form.is_valid(): 
           print('email:', form.cleaned_data['email']) 
           print('message:', form.cleaned_data['message']) 
           # do whatever you want to do, for example, send an email  
           return redirect('home')
   else: 
       form = ContactForm() 

   return render(request, "contact.html", {'form':form})
