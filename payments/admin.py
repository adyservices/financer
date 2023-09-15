from django.contrib import admin
from .models import Payments,Transactions
# Register your models here.

class PaymentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Payments._meta.fields]
    list_filter = ['event_id']
    list_per_page = 20
    ordering = ['id']

class TransactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transactions._meta.fields]
    list_filter = ['payment_id']
    list_per_page = 20
    ordering = ['id']

admin.site.register(Payments, PaymentsAdmin)
admin.site.register(Transactions, TransactionAdmin)



