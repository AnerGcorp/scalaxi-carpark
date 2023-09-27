from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.OwnerCarPark)
admin.site.register(models.CarPark)
admin.site.register(models.CarDriver)
admin.site.register(models.Car)
admin.site.register(models.CarRoute)