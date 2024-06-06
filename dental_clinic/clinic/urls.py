from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/new/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('dentists/', views.dentist_list, name='dentist_list'),
    path('dentists/new/', views.dentist_create, name='dentist_create'),
    path('dentists/<int:pk>/edit/', views.dentist_update, name='dentist_update'),
    path('dentists/<int:pk>/delete/', views.dentist_delete, name='dentist_delete'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/new/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('treatments/', views.treatment_list, name='treatment_list'),
    path('treatments/new/', views.treatment_create, name='treatment_create'),
    path('treatments/<int:pk>/edit/', views.treatment_update, name='treatment_update'),
    path('treatments/<int:pk>/delete/', views.treatment_delete, name='treatment_delete'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/new/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/edit/', views.invoice_update, name='invoice_update'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('feedbacks/new/', views.feedback_create, name='feedback_create'),
    path('feedbacks/<int:pk>/edit/', views.feedback_update, name='feedback_update'),
    path('feedbacks/<int:pk>/delete/', views.feedback_delete, name='feedback_delete'),
]
