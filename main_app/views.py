from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   return HttpResponse('<h1>Testing Testing</h1>')

def about(request):
   return HttpResponse('<h1>This is your ABOUT page</h1>')