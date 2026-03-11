from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect


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

def blog(request, slug):
    requested_blog = get_object_or_404(Blog, slug = slug)
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = requested_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info )
    comment = Comment.objects.filter(blog=requested_blog)
    comment_count = comment.count()
    context = {
        'blog' : requested_blog,
        'comments': comment,
        'comment_count' : comment_count,
    }

    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published' )
    context={
        'blogs' : blogs,
        'keyword' : keyword
    }
    return render(request, 'search.html', context)