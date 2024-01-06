from django.shortcuts import render,HttpResponse
from .  import models
from django.contrib.auth.decorators import login_required


def archive_list(request):
    blog=models.model_blog.objects.order_by('date')
    
    return render(request,'raadino/archive_list.html',{'blog':blog})




def single_detail(reqeust, slug):
    return HttpResponse(slug)
    single=models.model_blog.objects.get(slug=slug)
    return render(request,'raadino/single_detail.html',{'single':single})

