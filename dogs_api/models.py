from django.db import models

# Create your models here.
class DogInfo(models.Model):
    breed = models.CharField(max_length=500)
    org_img = models.CharField(max_length=500)
    mod_img = models.CharField(max_length=500)
    test_img = models.ImageField(null=True)

    def __breed__(self):
        return self.breed
    
    def __str_org_img__(self):
        return self.url
    
    def __str_mod_img__(self):
        return self.url