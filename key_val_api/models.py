from django.db import models

# Create your models here.
class KeyVal(models.Model):
    key = models.CharField(max_length=50)
    val = models.IntegerField(default=0)

    def __str__(self):
        return self.key

    def __str_val__(self):
        return self.val
