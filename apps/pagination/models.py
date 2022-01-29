from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def all_validations(self, post_data):
        errors={}
        f = self.validate_first_name(post_data, errors)
        l = self.validate_last_name(post_data, errors)
        e = self.validate_email(post_data, errors)
        return {**f, **l, **e}

    def validate_first_name(self, post_data, errors):
        if len(post_data['first_name'])<1:
            errors['first_name'] = "First name cannot be empty"
        elif len(post_data['first_name'])<2:
            errors['first_name'] = "First name must contain at least two letters"
        return errors

    def validate_last_name(self, post_data, errors):
        if len(post_data['last_name'])<1:
            errors['last_name'] = "Last name cannot be empty"
        elif len(post_data['last_name'])<2:
            errors['last_name'] = "Last name must contain at least two letters"
        return errors

    def validate_email(self, post_data, errors):
        if len(post_data['email'])<1:
            errors['email'] = "Email cannot be empty"
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Invalid email address'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()
