from django.db import models

# Create your models here.
class Review(models.Model):
    name        = models.CharField(max_length=120, null=True) # max_length = required
    description = models.TextField(blank=False, null=False) 
    email       = models.CharField(max_length=120, blank=True, null=True)