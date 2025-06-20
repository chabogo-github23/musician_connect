from django.db import models
from musicians.models import Musician

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    musicians = models.ManyToManyField(Musician, blank=True)

    def __str__(self):
        return self.name