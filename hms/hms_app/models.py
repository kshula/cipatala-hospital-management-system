# models.py

from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    insurance_provider = models.CharField(max_length=50, default='None')
    payment_method = models.CharField(max_length=50, default='None')
    preferred_language = models.CharField(max_length=50, default='None')
    religious_preferences = models.CharField(max_length=50,default='None')
    reason_for_visit = models.CharField(max_length=50,default='None')
    referring_physician = models.CharField(max_length=50,default='None')
    
    
    # Add other fields as needed

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add more doctor-related fields as needed

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.user.username

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('staff', 'Staff'), ('reception', 'Reception')])

    def __str__(self):
        return f'{self.user.username} - {self.user_type}'

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    recovery_chances = models.TextField()
    # Add more fields related to medical records

class LabTest(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    result = models.TextField()
    # Add more fields related to lab tests

class Complaint(models.Model):
    title = models.CharField(max_length=255)
    complaint_type = models.CharField(max_length=255)
    complaint_text = models.TextField()

    def __str__(self):
        return self.title  

# Add more models for Pharmacy, Inventory, etc.
