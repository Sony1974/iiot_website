from django.contrib import admin
from .models import Notifications

# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('machine', 'category', 'created')

admin.site.register(Notifications, NotificationAdmin)


