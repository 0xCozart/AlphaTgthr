from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.urls import path, re_path # url()
from .models import Post
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context={}, status=200)


def post_detail_view(request, post_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift/Java/iOS/Android
    return json data
    """
    print(post_id)
    data = {
        "id": post_id,
        # "content": obj.content,
        # "image_path": obj.image.url 
    }
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data['content'] = obj.content
    except: 
        data['message'] = "Not Found"
        status = 404
    
    # return HttpResponse(f"<h1>{post_id} - {obj.content}</h1>")
    return JsonResponse(data, status=status) #Json.dumps content_type="application/json"