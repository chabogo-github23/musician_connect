from django.contrib import admin
from .models import Musician

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'instrument', 'location', 'is_professional', 'rating')
    list_filter = ('genre', 'instrument', 'availability', 'rating')
    search_fields = ('name', 'bio', 'location')
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'name', 'bio', 'rating')
        }),
        ('Musical Details', {
            'fields': ('genre', 'instrument', 'years_experience', 'sample_work')
        }),
        ('Availability & Rates', {
            'fields': ('availability', 'available_from', 'available_to', 'hourly_rate')
        }),
        ('Contact & Social', {
            'fields': ('location', 'website', 'instagram', 'twitter'),
            'classes': ('collapse',)
        })
    )
    readonly_fields = ('is_professional',)
    
    def is_professional(self, obj):
        return obj.is_professional()
    is_professional.boolean = True
    is_professional.short_description = 'Pro?'

admin.site.register(Musician, MusicianAdmin)