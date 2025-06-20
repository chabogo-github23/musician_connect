from django.contrib import admin
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'location')
    fieldsets = (
        ('User', {
            'fields': ('user', 'phone', 'address')
        }),
        ('Account Type', {
            'fields': ('account_type',)
        }),
        ('Notifications', {
            'fields': ('location', 'instruments', 'genres', 'profile_pic')
        }),
    )

class EmailAdminAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'autofocus': True}))
    
    def clean_username(self):
        email = self.cleaned_data.get('username')
        return email

admin.site.register(User)
admin.site.login_form = EmailAdminAuthenticationForm