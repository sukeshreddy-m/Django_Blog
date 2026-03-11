from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

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

def post(request):
    posts = Blog.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'dashboards/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect('posts')
        else:
            print("Form is invalid")
            print(form.errors)
    form = BlogPostForm()   
    context = {
        'form' : form,
    }
    return render(request, 'dashboards/add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) +'-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form' : form,
        'post' : post,
    }
    return render(request, 'dashboards/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')