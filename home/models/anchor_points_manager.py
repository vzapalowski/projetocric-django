from django.db import models
from core.models import Anchorpoint


class AnchorPointsManager(models.Model):
    anchor_point = models.OneToOneField(Anchorpoint, on_delete=models.CASCADE)
