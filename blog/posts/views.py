from django.shortcuts import render
from .models import blog
# Create your views here.

def home(request):
    posts = blog.objects.all()
    
    return render(request,'home.html',{'post':posts})
