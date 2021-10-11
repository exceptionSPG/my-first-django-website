from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request,'home.html',{'name':'exceptionSPG'})

def add(request):
  #we need to bypass csrf middleware
 
  val1 = int(request.POST['num1'])
  val2 = int(request.POST['num2'])
  res = val1+val2
  return render(request,'result.html',{'res': res})
