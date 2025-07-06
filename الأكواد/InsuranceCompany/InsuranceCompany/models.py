# models.py
from django.db import models

class InsuranceCompany(models.Model):
    insurance_id = models.CharField(max_length=100, unique=True)
    coverage_type = models.CharField(max_length=100)
    contact_info = models.TextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
