from django.db import models

class PatientRegistration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    organ = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile_number = models.CharField(max_length=15)  

    def __str__(self):
        return self.name
    
from django.db import models

class DonarRegistration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    ORGAN_CHOICES = [
        ('Any part of my body', 'Any part of my body'),
        ('Lungs', 'Lungs'),
        ('Blood', 'Blood'),
        ('Kidney', 'Kidney'),
        ('Liver', 'Liver'),
        ('Heart', 'Heart'),
        ('Eyes', 'Eyes'),
    ]

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    organs_to_donate = models.CharField(max_length=50, choices=ORGAN_CHOICES)  
    address = models.CharField(max_length=300)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    mobile_number = models.CharField(max_length=15)  

    def __str__(self):
        return self.name
