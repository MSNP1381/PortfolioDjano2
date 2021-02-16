from django.shortcuts import render ,get_object_or_404 # ,HttpResponse
from .models import Blog_model


def all_blogs(request):
    blog_obj = Blog_model.objects

    return render(request, 'allblogs.html', {'blog_obj_all': blog_obj.all()})


def blog_detail(request, blog_id):
    obj = get_object_or_404(Blog_model,pk=blog_id)
    return render(request, "blog_details.html", {'obj1': obj})
