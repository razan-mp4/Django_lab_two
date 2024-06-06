from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Dentist, Appointment, Treatment, Invoice, Feedback
from .forms import PatientForm, DentistForm, AppointmentForm, TreatmentForm, InvoiceForm, FeedbackForm

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test



def custom_logout_view(request):
    logout(request)
    return redirect('login')
# Helper functions to check user roles
def is_admin(user):
    return user.groups.filter(name='admin').exists()

def is_dentist(user):
    return user.groups.filter(name='dentist').exists()

def is_receptionist(user):
    return user.groups.filter(name='Receptionist').exists()

# Home view with debug statement
def home(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Dentist: {is_dentist(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    return render(request, 'clinic/home.html')

# Patient views
@login_required
@user_passes_test(is_admin)
def patient_list(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    patients = Patient.objects.all()
    return render(request, 'clinic/patient_list.html', {'patients': patients})

@login_required
@user_passes_test(is_admin)
def patient_create(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinic/patient_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def patient_update(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'clinic/patient_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def patient_delete(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'clinic/patient_confirm_delete.html', {'object': patient})

# Dentist views
@login_required
@user_passes_test(is_admin)
def dentist_list(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    dentists = Dentist.objects.all()
    return render(request, 'clinic/dentist_list.html', {'dentists': dentists})

@login_required
@user_passes_test(is_admin)
def dentist_create(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    if request.method == 'POST':
        form = DentistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dentist_list')
    else:
        form = DentistForm()
    return render(request, 'clinic/dentist_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def dentist_update(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    dentist = get_object_or_404(Dentist, pk=pk)
    if request.method == 'POST':
        form = DentistForm(request.POST, instance=dentist)
        if form.is_valid():
            form.save()
            return redirect('dentist_list')
    else:
        form = DentistForm(instance=dentist)
    return render(request, 'clinic/dentist_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def dentist_delete(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    dentist = get_object_or_404(Dentist, pk=pk)
    if request.method == 'POST':
        dentist.delete()
        return redirect('dentist_list')
    return render(request, 'clinic/dentist_confirm_delete.html', {'object': dentist})

# Appointment views
@login_required
@user_passes_test(lambda u: is_admin(u) or is_dentist(u) or is_receptionist(u))
def appointment_list(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Dentist: {is_dentist(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    appointments = Appointment.objects.all()
    return render(request, 'clinic/appointment_list.html', {'appointments': appointments})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_receptionist(u))
def appointment_create(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'clinic/appointment_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_receptionist(u))
def appointment_update(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'clinic/appointment_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def appointment_delete(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'clinic/appointment_confirm_delete.html', {'object': appointment})

# Treatment views
@login_required
@user_passes_test(is_admin)
def treatment_list(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    treatments = Treatment.objects.all()
    return render(request, 'clinic/treatment_list.html', {'treatments': treatments})

@login_required
@user_passes_test(is_admin)
def treatment_create(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treatment_list')
    else:
        form = TreatmentForm()
    return render(request, 'clinic/treatment_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def treatment_update(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    treatment = get_object_or_404(Treatment, pk=pk)
    if request.method == 'POST':
        form = TreatmentForm(request.POST, instance=treatment)
        if form.is_valid():
            form.save()
            return redirect('treatment_list')
    else:
        form = TreatmentForm(instance=treatment)
    return render(request, 'clinic/treatment_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def treatment_delete(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    treatment = get_object_or_404(Treatment, pk=pk)
    if request.method == 'POST':
        treatment.delete()
        return redirect('treatment_list')
    return render(request, 'clinic/treatment_confirm_delete.html', {'object': treatment})

# Invoice views
@login_required
@user_passes_test(is_admin)
def invoice_list(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    invoices = Invoice.objects.all()
    return render(request, 'clinic/invoice_list.html', {'invoices': invoices})

@login_required
@user_passes_test(is_admin)
def invoice_create(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'clinic/invoice_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def invoice_update(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'clinic/invoice_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def invoice_delete(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'clinic/invoice_confirm_delete.html', {'object': invoice})

# Feedback views
@login_required
@user_passes_test(lambda u: is_admin(u) or is_dentist(u) or is_receptionist(u))
def feedback_list(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Dentist: {is_dentist(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    feedbacks = Feedback.objects.all()
    return render(request, 'clinic/feedback_list.html', {'feedbacks': feedbacks})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_receptionist(u))
def feedback_create(request):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'clinic/feedback_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: is_admin(u) or is_receptionist(u))
def feedback_update(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    print(f"Is Receptionist: {is_receptionist(request.user)}")
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'clinic/feedback_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def feedback_delete(request, pk):
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    print(f"Is Admin: {is_admin(request.user)}")
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback_list')
    return render(request, 'clinic/feedback_confirm_delete.html', {'object': feedback})
