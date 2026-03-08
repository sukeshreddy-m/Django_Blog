from django.shortcuts import render
from blogs.models import Category, Blog
from assignments.models import about

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