# Generated by Django 5.0.6 on 2024-06-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('bio', models.TextField(max_length=150)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profile_image', models.ImageField(null=True, upload_to='static/img/')),
            ],
        ),
    ]
