from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'organizer', 'date', 'location', 'budget', 'musicians_count')
    list_filter = ('genre', 'date', 'location')
    search_fields = ('name', 'organizer', 'location')
    filter_horizontal = ('musicians',)
    
    def musicians_count(self, obj):
        return obj.musicians.count()
    musicians_count.short_description = 'Musicians'

admin.site.register(Event, EventAdmin)