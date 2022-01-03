from django.db import models
from django.urls import reverse
from datetime import date

TOD = (
   ('M', 'Morning'),
   ('A', 'Afternoon'),
   ('E', 'Evening')
)


class Fertilizer(models.Model):
   name = models.CharField(max_length=25)
   description = models.CharField(max_length=200)
   effects = models.CharField(max_length=25)

   def __str__(self) -> str:
      return self.name

   def get_absolute_url(self):
      return reverse("fertilizers_detail", kwargs={"pk": self.id})


class Plant(models.Model):
   name = models.CharField(max_length=20)
   description = models.CharField(max_length=200)
   type = models.CharField(max_length=20)
   price = models.IntegerField()
   fertilizers = models.ManyToManyField(Fertilizer)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse("plants_detail", kwargs={"plant_id": self.id})

   def watered_for_today(self):
      return self.watering_set.filter(date=date.today()).count() >= len(TOD)


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
