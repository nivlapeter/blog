from django.shortcuts import render
from .models import Post


# Create your views here.
def Home(request):
    context = {
        'posts' : Post.objects.all()

    }
    return render(request, 'the_blog/home.html',context)

def About(request):
    return render(request,'the_blog/about.html', {'title':'About'})