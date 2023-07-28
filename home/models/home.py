from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=50, default= -29.95)
    lng = models.CharField(max_length=50, default= 51.64)

    def __str__(self):
        return self.name
    