from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
# Create your views here.

def home_view(request, post_id, *args, **kwargs):
    obj = Post.objects.get (id=post_id)
    return HttpResponse(f"<h1>{post_id} - {obj.content}</h1>")