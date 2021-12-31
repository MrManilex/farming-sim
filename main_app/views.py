from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant


def home(request):
   return render(request, 'home.html')


def about(request):
   return render(request, 'about.html')


def plants_index(request):
   plants = Plant.objects.all()
   return render(request, 'plants/index.html', { 'plants': plants })

