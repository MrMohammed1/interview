from django.db import models

# Create your models here.

class Person(models.Model):
    personID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    nationalityID = models.IntegerField()
    birthDate = models.DateTimeField()