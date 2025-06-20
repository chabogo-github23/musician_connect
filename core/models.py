from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Profile(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('musician', 'Musician'),
        ('band', 'Band'),
        ('industry', 'Industry Professional'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='core_profile'
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE_CHOICES,
        default='musician'
    )
    bio = models.TextField(
        blank=True,
        help_text='Tell us about your musical background'
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        help_text='Where are you based?'
    )
    instruments = models.CharField(
        max_length=200,
        blank=True,
        help_text='What instruments do you play? (separate with commas)'
    )
    genres = models.CharField(
        max_length=200,
        blank=True,
        help_text='What genres do you specialize in? (separate with commas)'
    )
    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        help_text='Upload a profile picture (optional)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    payments = models.TextField(blank=True)
    rentals = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.get_account_type_display()})"

    @property
    def display_name(self):
        return self.user.first_name or self.user.username

    class Meta:
        ordering = ['-created_at']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        db_table = 'auth_user'
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    def __str__(self):
        return self.email
