from django.db import models
from django.urls import reverse


class Plant(models.Model):
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=100)
   type = models.CharField(max_length=20)
   price = models.IntegerField()

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse("plants_detail", kwargs={"plant_id": self.id})
