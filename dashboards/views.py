from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

@login_required(login_url='login')
def dashboard(request):
    categories_count = Category.objects.all().count()
    posts = Blog.objects.all().count()
    context = {
        'categories_count' : categories_count,
        'posts':posts,
    }
    return render(request, 'dashboards/dashboard.html', context)

def categories(request):
    return render(request, 'dashboards/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form' : form,
    }
    return render(request, 'dashboards/add_category.html', context)

def edit_category(request, pk):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=pk)
        new = request.POST['c_name']
        category.category_name = new
        category.save()
        return redirect('categories')
    category = get_object_or_404(Category, pk=pk)
    context ={
        'category' : category
    }
    return render(request, 'dashboards/edit.html', context)

def delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')