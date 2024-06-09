from django.db import models
from django.urls import reverse


class Projects(models.Model):
    
    img_url = models.CharField(max_length= 1000)
    url = models.CharField(max_length= 1000)
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
