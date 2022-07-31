from django.db import models

# Create your models here.

class Notifications(models.Model):

    CATEGORY_CHOICES = (
        ('Electrical', 'Electrical'),
        ('Mechanical', 'Mechanical'),
    )
    machine = models.CharField(max_length=10)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name    = 'notification'
        verbose_name_plural = 'notifications'
        ordering = ['-created']

    def __str__(self):
        return self.machine
