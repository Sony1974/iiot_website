from django.db import models

# Create your models here.

class Notifications(models.Model):
    machine = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.machine
