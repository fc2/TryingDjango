from django.shortcuts import render
from django.utils import timezone
from .models import Post

#dot means current directory or current application.
#view is where we put the "logic"
# Create your views here.

def post_list(request):
    #using QuerySet to get the posts from the database
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
