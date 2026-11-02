from django.contrib import admin
from .models import Prescription, Medicine


class MedicineInline(admin.TabularInline):
    model = Medicine
    extra = 1


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'issued_on')
    inlines = [MedicineInline]
