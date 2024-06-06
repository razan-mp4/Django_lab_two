from django import forms
from .models import Patient, Dentist, Appointment, Treatment, Invoice, Feedback

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
