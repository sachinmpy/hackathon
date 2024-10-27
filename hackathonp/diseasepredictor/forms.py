from django.forms import ModelForm
from .models import HealthData

class HealthDataForm(ModelForm):

    class Meta:
        model = HealthData
        fields = '__all__'

