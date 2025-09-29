from django.db import models
from cities.models import AnchorPoint


class AnchorPointsManager(models.Model):
    anchor_point = models.OneToOneField(AnchorPoint, on_delete=models.CASCADE)
