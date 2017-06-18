from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    for count, post in enumerate(posts):
        print post
        print post.pub_date
        print post.slug
        posts_lists.append("NO.{}:".format(str(count)) + str(post) + "<br />")
    return HttpResponse(posts_lists)
