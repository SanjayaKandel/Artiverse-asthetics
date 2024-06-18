from django.db import models
from Artists.models import Artist
# Create your models here.

    
class Artwork(models.Model):
    MEDIUM_CHOICES = [
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('photography', 'Photography'),
    ]
    title = models.CharField(max_length=100)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100, choices=MEDIUM_CHOICES)
    year_created = models.IntegerField()
    image = models.ImageField(upload_to='static/img/', null=True)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title