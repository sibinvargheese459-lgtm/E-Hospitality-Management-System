from django.db import models
from patients.models import Patient
from appointments.models import Appointment


class Bill(models.Model):
    class PaymentStatus(models.TextChoices):
        UNPAID = 'UNPAID', 'Unpaid'
        PAID = 'PAID', 'Paid'
        PARTIAL = 'PARTIAL', 'Partially Paid'

    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CARD = 'CARD', 'Card'
        UPI = 'UPI', 'UPI'
        INSURANCE = 'INSURANCE', 'Insurance'

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='bills')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='bills')
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medicine_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices,
                                       default=PaymentStatus.UNPAID)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices, blank=True)
    generated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-generated_on']

    @property
    def total_amount(self):
        return (self.consultation_fee + self.medicine_charges + self.other_charges) - self.discount

    def __str__(self):
        return f"Bill #{self.pk} - {self.patient} - {self.total_amount}"
