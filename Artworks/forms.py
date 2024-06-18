from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'medium', 'year_created', 'image', 'description', 'price']
        widgets = {
            'medium': forms.Select(choices=[('Sculpture', 'Sculpture'), ('Painting', 'Painting'), ('Photography', 'Photography')]),
        }
