# -*- coding:utf-8 -*-
import sys
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    posts_lists = list()
    now = datetime.now()
    html = template.render(locals())
    print sys.getdefaultencoding()
    #for count, post in enumerate(posts):
    #    print post
    #    print post.pub_date
    #    print post.slug
    #    #posts_lists.append("NO.{}:".format(str(count)) + str(post) + "<br />")
    #    posts_lists.append("NO.{}:".format(str(count)) + str(post) + "<hr />")
    #    posts_lists.append("<small>" + str(post.body) + "</small><br /><br />")
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug = slug)
        print post
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/homepage/')





