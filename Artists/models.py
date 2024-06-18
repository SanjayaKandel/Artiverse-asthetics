from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='static/img/', null=True)
    def __str__(self):
        return self.name