from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('patient', 'total_amount', 'payment_status', 'payment_method', 'generated_on')
    list_filter = ('payment_status', 'payment_method')
