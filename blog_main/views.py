from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    featured_blogs = Blog.objects.filter(is_featured = True)
    posts = Blog.objects.filter(is_featured = False, status = 'Published')
    context = {
        'featured_blogs':featured_blogs,
        'posts':posts,
    }
    return render(request, 'home.html', context)