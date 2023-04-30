from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MyRegistrationForm, MyLoginForm

def home(request):
    return render(request, 'home.html', {'user': request.user})

def myregister(request):
    if request.method == 'POST':
        form = MyRegistrationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})

def mylogin(request):
    if request.method == 'POST':
        form = MyLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = MyLoginForm()
    return render(request, 'login.html', {'form': form})


def mylogout(request):
    logout(request)
    return redirect('home')