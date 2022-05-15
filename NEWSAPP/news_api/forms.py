from django.forms import ModelForm
from .models import NewsDB

class CreateNewsForm(ModelForm):
    class Meta:
        model = NewsDB
        fields = '__all__'
        exclude = ['time', 'by',]
        