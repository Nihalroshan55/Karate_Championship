# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fees = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username


        
class Candidate(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    COLOUR_BELT = 'Colour Belt'
    BLACK_BELT = 'Black Belt'
    BELT_CHOICES = [
        (COLOUR_BELT, 'Colour Belt'),
        (BLACK_BELT, 'Black Belt'),
    ]

    KUMITE = 'Kumite'
    KATA = 'Kata'

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    belt_color = models.CharField(max_length=20, choices=BELT_CHOICES)
    weight = models.FloatField()
    kata = models.BooleanField(default=False)
    kumite = models.BooleanField(default=False)
    category = models.CharField(max_length=20, blank=True, null=True)
    weight_category = models.CharField(max_length=20, blank=True, null=True)
    entry_fee=models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name
