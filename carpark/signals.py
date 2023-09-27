from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Car, CarPark


@receiver(post_save, sender=Car)
def create_car(sender, instance, created, **kwargs):
    if created:
        obj = Car.objects.filter(park=instance.park)
        instance.park.total_cars = len(obj)
        instance.park.save()

@receiver(post_delete, sender=Car)
def create_car(sender, instance, using, **kwargs):
    if using:
        obj = Car.objects.filter(park=instance.park)
        instance.park.total_cars = len(obj)
        instance.park.save()




# @receiver(pre_delete, sender=Car)
# def delete_car(sender, instance, **kwargs):
#         instance.profile.save()