from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def hello_html(request):
    context={
        'tile': 'Full Stack Tutorials',
        'section':'Introduction to Django',
        'abstract': 'this is an abstract',
        'text_body': 'this is a text body',
        'posts':['post1','post2','post3']
    }
    return render(request, 'hello_world.html', context=context)

