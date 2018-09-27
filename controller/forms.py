from django import forms
from .models import AppointmentModel


class AppointmentModelForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel

        fields = ['appointment_name', 'appointment_date', 'appointment_phone', 'appointment_message']
