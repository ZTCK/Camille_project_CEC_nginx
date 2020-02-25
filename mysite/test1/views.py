from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #list = Post.objects.order_by('-pub_date')[:5]
    #context = {'list': list}
    return render(request, 'test1/index.html')

def debug(request):
    #list = Post.objects.order_by('-pub_date')[:5]
    #context = {'list': list}
    return render(request, 'test1/debug.html')

def logcapture(request):
    return render(request, 'test1/logcapture.html')
