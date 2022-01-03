from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from main_app.forms import WateringForm
from .models import Fertilizer, Plant, Watering
from django.contrib.auth.views import LoginView


def home(request):
   return render(request, 'home.html')


def about(request):
   return render(request, 'about.html')


def plants_index(request):
   plants = Plant.objects.all()
   return render(request, 'plants/index.html', {'plants': plants})


def plants_detail(request, plant_id):
   plant = Plant.objects.get(id=plant_id)
   fertilizers_plant_doesnt_have = Fertilizer.objects.exclude(
      id__in=plant.fertilizers.all().values_list('id'))
   watering_form = WateringForm()
   return render(request, 'plants/detail.html', {'plant': plant, 'watering_form': watering_form, 'fertilizers': fertilizers_plant_doesnt_have})


def add_watering(request, plant_id):
   form = WateringForm(request.POST)
   if form.is_valid():
      new_watering = form.save(commit=False)
      new_watering.plant_id = plant_id
      new_watering.save()
   return redirect('plants_detail', plant_id=plant_id)


def assoc_fertilizer(request, plant_id, fertilizer_id):
   Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
   return redirect('plants_detail', plant_id=plant_id)


class PlantCreate(CreateView):
   model = Plant
   fields = ['name', 'description', 'type', 'price']
   def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)


class PlantUpdate(UpdateView):
   model = Plant
   fields = ['description', 'type', 'price']


class PlantDelete(DeleteView):
   model = Plant
   success_url = '/plants/'


class FertilizerCreate(CreateView):
   model = Fertilizer
   fields = '__all__'


class FertilizerList(ListView):
   model = Fertilizer


class FertilizerDetail(DetailView):
   model = Fertilizer


class FertilizerUpdate(UpdateView):
   model = Fertilizer
   fields = ['effects', 'description']


class FertilizerDelete(DeleteView):
   model = Fertilizer
   success_url = '/fertilizers/'


class Home(LoginView):
   template_name = 'home.html'