from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Musician(models.Model):
    GENRE_CHOICES = [
        ('GOSPEL', 'Gospel'),
        ('ROCK', 'Rock'),
        ('POP', 'Pop'),
        ('JAZZ', 'Jazz'),
        ('CLASSICAL', 'Classical'),
        ('HIPHOP', 'Hip Hop'),
        ('ELECTRONIC', 'Electronic'),
        ('OTHER', 'Other'),
    ]
    
    INSTRUMENT_CHOICES = [
        ('GUITAR', 'Guitar'),
        ('PIANO', 'Piano'),
        ('DRUMS', 'Drums'),
        ('BASS', 'Bass'),
        ('VIOLIN', 'Violin'),
        ('VOICE', 'Voice'),
        ('OTHER', 'Other'),
    ]
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='musician_profile'
    )
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    instrument = models.CharField(max_length=100, choices=INSTRUMENT_CHOICES)
    location = models.CharField(max_length=100)
    years_experience = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    availability = models.BooleanField(default=True)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)
    bio = models.TextField()
    sample_work = models.URLField(blank=True, null=True)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        null=True,
        blank=True
    )
    website = models.URLField(blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def is_professional(self):
        return self.years_experience >= 5
    
    @property
    def social_links(self):
        return {
            'website': self.website,
            'instagram': f"https://instagram.com/{self.instagram}" if self.instagram else None,
            'twitter': f"https://twitter.com/{self.twitter}" if self.twitter else None
        }