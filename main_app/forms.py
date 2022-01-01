from django.forms import ModelForm
from .models import Feeding, Watering

class FeedingForm(ModelForm):
   class Meta:
      model = Watering
      fields = ['date', 'tod']