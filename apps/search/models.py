from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female')
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Male)
    image = models.CharField(max_length=100, blank=False, null=False)
    Basketball = 'basketball'
    Football = 'football'
    Baseball = 'baseball'
    Cricket = 'cricket'
    Hockey = 'hockey'
    SPORT_CHOICES = (
        (Basketball, 'Basketball'),
        (Football, 'Football'),
        (Baseball, 'Baseball'),
        (Cricket, 'Cricket'),
        (Hockey, 'Hockey')
    )
    sport = models.CharField(max_length=10, choices=SPORT_CHOICES, default=Basketball)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #objects = UsersManager()
    def __repr__(self) -> str:
        return "<Users object: {} {} {} {} {}>".format(self.first_name, self.last_name, self.gender, self.image, self.sport)
