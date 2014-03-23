from django.db import models

# Create your models here.
class Kitten(models.Model):

  name = models.CharField(max_length = 255)
  breed = models.CharField(max_length = 255)
