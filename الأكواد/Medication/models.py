from django.db import models

class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

    def __str__(self):
        return self.name
