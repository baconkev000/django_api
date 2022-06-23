from django.db import models

# Create your models here.
class DogInfo(models.Model):
    breed = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    img = models.ImageField()

    def __str__(self):
        return self.breed
    
    def __str_url__(self):
        return self.url