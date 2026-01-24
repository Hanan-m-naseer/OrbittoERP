from django.db import models
from apps.common.models import TimeStampedModel


# Create your models here.

class Company(TimeStampedModel):
    name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255, blank=True)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    address = models.TextField(blank=True)
    country = models.CharField(max_length=100)

    currency = models.CharField(max_length=10, default="USD")
    timezone = models.CharField(max_length=50, default="UTC")

    tax_id = models.CharField(max_length=50, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
