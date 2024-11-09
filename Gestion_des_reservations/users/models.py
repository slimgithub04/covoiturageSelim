from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=100, default='Unknown')
    lastname = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
