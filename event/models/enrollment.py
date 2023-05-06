from django.db import models


class Bond(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bond_choice = models.ForeignKey(Bond, on_delete=models.CASCADE)
    how_knew = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    route = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    def get_bond_choice_display(self):
        if isinstance(self.bond_choice, str):
            return self.bond_choice.upper()
        else:
            return "-"