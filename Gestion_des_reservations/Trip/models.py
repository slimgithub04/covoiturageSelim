# models.py
from django.db import models

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateTimeField(null=False)  # Utilisez DateTimeField ou DateField selon votre besoin

    def __str__(self):
        return f"{self.destination} - {self.departure_date}"





