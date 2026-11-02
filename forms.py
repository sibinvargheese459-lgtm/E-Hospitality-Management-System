from django import forms
from hms_project.formutils import BootstrapFormMixin
from .models import Bill


class BillForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient', 'appointment', 'consultation_fee', 'medicine_charges',
                  'other_charges', 'discount', 'payment_status', 'payment_method']
