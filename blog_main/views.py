from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from assignments.models import about
from .form import Registration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_blogs = Blog.objects.filter(is_featured = True)
    posts = Blog.objects.filter(is_featured = False, status = 'Published')
    try:
        About = about.objects.get()
    except:
        About = None
    context = {
        'featured_blogs':featured_blogs,
        'posts':posts,
        'about' : About
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
                'form' : form,
            }
            return render(request, 'register.html', context)
    form = Registration()
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')