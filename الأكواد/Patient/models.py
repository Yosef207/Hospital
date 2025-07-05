from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name
