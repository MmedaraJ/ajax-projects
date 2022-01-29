from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import CharField

class PostManager(models.Manager):
    def post_validations(self, post_data):
        errors = {}
        if len(post_data['post']) < 1:
            errors['post'] = "Post cannot be empty"
        return errors

class Post(models.Model):
    post = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
