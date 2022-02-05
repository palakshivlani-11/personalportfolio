from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1000)
    def __str__(self):
         return self.name

    class Meta:
        verbose_name_plural = "Contact Responses"
