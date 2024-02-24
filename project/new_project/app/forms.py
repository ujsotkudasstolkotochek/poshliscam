from django.forms import ModelForm
from .models import Bin

class BinForm(ModelForm):
    class Meta:
        model = Bin
        fields = '__all__'