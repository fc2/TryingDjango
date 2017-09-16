from django.shortcuts import render

#view is where we put the "logic"
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
