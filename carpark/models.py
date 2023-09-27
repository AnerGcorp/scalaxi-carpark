# We can write models with sql, but it's not very efficient
# that's why I will use ORM(object relational mapping), I will
# use django

from django.db import models
from django.utils.translation import gettext_lazy as _

class Person(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max:100")
        )
    surname = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Surname"),
        help_text=_("format: required, max:100")
    )
    last_name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Lastname"),
        help_text=_("format: required, max:100")
    )
    phone_number = models.CharField(
        max_length=12,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Phone number"),
        help_text=_("format: required, max:100")
    )

class OwnerCarPark(Person):
    class Meta:
        verbose_name = _("Car Park Owner")
        verbose_name_plural = _("Car Park Owners")


class CarPark(models.Model):
    class Meta:
        verbose_name = _("Car Park")
        verbose_name_plural = _("Car Parks")
    owner = models.ForeignKey('OwnerCarPark', on_delete=models.CASCADE, related_name="owner_park")
    park_name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Car Park Name"),
        help_text=_("format: required, max:100")
    )
    total_cars = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("number/qty of cars"),
        help_text=_("format: required, default-0"),
    )


class CarDriver(Person):
    class Meta:
        verbose_name = _("Car Driver")
        verbose_name_plural = _("Car Driver")

    car = models.OneToOneField("Car", on_delete=models.PROTECT, related_name="car")


class Car(models.Model):
    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    plate_number = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("License Number"),
        help_text=_("format: required, max:50")
    )
    park = models.ForeignKey("CarPark", on_delete=models.CASCADE, related_name="park")
    route = models.OneToOneField("CarRoute", on_delete=models.CASCADE, related_name="route")

class CarRoute(models.Model):
    class Meta:
        verbose_name = _("Route")
        verbose_name_plural = _("Routes")
    path = models.TextField(
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Route"),
        help_text=_("format: required")
    )


