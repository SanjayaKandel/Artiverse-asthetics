# Generated by Django 5.0.6 on 2024-06-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0002_remove_artwork_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/'),
        ),
    ]