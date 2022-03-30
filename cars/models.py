from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name