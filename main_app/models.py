from django.db import models
from django.urls import reverse

MEALS = (
   ('M', 'Morning'),
   ('A', 'Afternoon'),
   ('E', 'Evening')
)


class Plant(models.Model):
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=200)
   type = models.CharField(max_length=20)
   price = models.IntegerField()

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse("plants_detail", kwargs={"plant_id": self.id})


class Watering(models.Model):
   date = models.DateField()
   meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
   )

   def __str__(self):
      return f'{self.get_meal_display()} on {self.date}'
