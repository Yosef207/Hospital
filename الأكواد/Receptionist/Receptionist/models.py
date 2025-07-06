from django.db import models

class Receptionist(models.Model):
    joptitle = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    receptionist_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
