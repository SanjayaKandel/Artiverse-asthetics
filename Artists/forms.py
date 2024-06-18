from django import forms
from .models import Artist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'phone','email', 'profile_image']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']