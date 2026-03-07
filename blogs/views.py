from django.shortcuts import render, redirect
from .models import Blog, Category

def posts_by_category(request, category_id):
    blogs_by_categories = Blog.objects.filter(category_id=category_id)
    try:
        category = Category. objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'blogs_by_categories' : blogs_by_categories,
        'category' : category,
    }
    return render(request, 'posts_by_category.html', context)