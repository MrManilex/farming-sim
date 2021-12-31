from django.shortcuts import render
from django.http import HttpResponse


def home(request):
   return render(request, 'home.html')


def about(request):
   return render(request, 'about.html')


def plants_index(request):
   return render(request, 'plants/index.html', { 'plants': plants })


class Plant: 
   def __init__(self, name, description, type, price):
      self.name = name
      self.description = description
      self.type = type
      self.price = price


plants = [
   Plant('Lolo', 'green', 'Kinda rude.', 3),
   Plant('Sachi', 'hairy', 'Looks like a turtle.', 0),
   Plant('Fancy', 'blue', 'Happy fluff ball.', 4),
   Plant('Bonk', 'soft', 'Meows loudly.', 6)
]
