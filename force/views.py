from django.shortcuts import render
from django.http import HttpResponse
from.models import info
def pro(request):
    product=info.objects.all()
    return render(request,'index.html',{'prod':product})

# Create your views here.
def login(request):
    return HttpResponse("<h1>welcome</h1>"
                        "<p>welcome all</p>")
def reg(request):
    return HttpResponse("<h1>register page </h1>")

