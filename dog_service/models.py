from django.db import models
from django.forms import CharField, ImageField

# Create your models here.
class DogInfo(models.Model):
    breed = CharField(max_length='100')
    img = ImageField()