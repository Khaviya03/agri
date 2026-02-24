from django.db import models
from django.conf import settings

class Waste(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    estimated_value = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='waste_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.waste_type