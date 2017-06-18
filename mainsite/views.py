# -*- coding:utf-8 -*-
import sys
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    print sys.getdefaultencoding()
    for count, post in enumerate(posts):
        print post
        print post.pub_date
        print post.slug
        #posts_lists.append("NO.{}:".format(str(count)) + str(post) + "<br />")
        posts_lists.append("NO.{}:".format(str(count)) + str(post) + "<hr />")
        posts_lists.append("<small>" + str(post.body) + "</small><br /><br />")
    return HttpResponse(posts_lists)
