from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_method', 'timestamp', 'is_successful')
    search_fields = ('user__username',)
    list_filter = ('payment_method', 'is_successful')

admin.site.register(Payment, PaymentAdmin)
