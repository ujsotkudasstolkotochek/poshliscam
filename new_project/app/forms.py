from django.forms import ModelForm
from .models import Bin, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BinForm(ModelForm):
    class Meta:
        model = Bin
        fields = '__all__'
        exclude = ['host', 'likes', 'bin_is_liked']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio']