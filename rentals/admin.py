from django.contrib import admin
from .models import Instrument, Rental

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'rental_price', 'is_available')
    search_fields = ('name', 'owner__username')
    list_filter = ('is_available',)

class RentalAdmin(admin.ModelAdmin):
    list_display = ('instrument', 'renter', 'start_date', 'end_date', 'is_confirmed')
    search_fields = ('instrument__name', 'renter__username')
    list_filter = ('is_confirmed',)

admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Rental, RentalAdmin)
