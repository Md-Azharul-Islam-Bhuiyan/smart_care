from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime


APPOINMENT_TYPE = [
    ('Offline','Offline'),
    ('Online','Online'),
]
APPOINMENT_STATUS = [
    ('Pending','Pending'),
    ('Running','Running'),
    ('Completed','Completed'),
]



class Appoinment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appoinment_type = models.CharField(max_length=30, choices=APPOINMENT_TYPE)
    appoinment_status = models.CharField(max_length=30, choices=APPOINMENT_STATUS, default="Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name}  Patient: {self.patient.user.first_name}"
    