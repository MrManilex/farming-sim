from django.db import models
from django.urls import reverse

TOD = (
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
   date = models.DateField('Watering Date')
   tod = models.CharField(
      max_length=1,
      choices=TOD,
      default=TOD[0][0]
   )

   plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

   def __str__(self):
      return f'{self.get_tod_display()} on {self.date}'
   
   class Meta:
      ordering = ['-date']
