from django.db import models

class Appointment(models.Model):
       STATUS_CHOICES = [
           ('pending', 'Pending'),
           ('confirmed', 'Confirmed'),
           ('canceled', 'Canceled'),
       ]

       status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
       time = models.DateTimeField()
       age = models.PositiveIntegerField()
       appointment_id = models.AutoField(primary_key=True)

       def __str__(self):
           return f"Appointment {self.appointment_id} - Status: {self.status}"