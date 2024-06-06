from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)

class Dentist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=50)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField()

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Feedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()