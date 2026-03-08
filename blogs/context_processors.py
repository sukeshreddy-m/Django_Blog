from .models import Category
from assignments.models import social

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)

def social_links(request):
    Social = social.objects.all()
    return dict(Social=Social)