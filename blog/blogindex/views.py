from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import blogPost
# Create your views here.
def blogindex(request):
	posts = blogPost.objects.all()
	return render(request,'index.html',{'posts': posts})


def singlePost(request, pk):
    post = get_object_or_404(blogPost, pk=pk)
    return render(request, 'single-post.html', {'post': post})

def aboutUs(request):
	return HttpResponse("This is about us page")