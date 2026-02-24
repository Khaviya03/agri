from django.db import models
from django.conf import settings

class Crop(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    price_per_kg = models.FloatField()
    harvest_date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name