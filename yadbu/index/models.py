from django.db import models

class Identity(models.Model):
    patient_number = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

class Attributes(models.Model):
    patient_identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.IntegerField()

