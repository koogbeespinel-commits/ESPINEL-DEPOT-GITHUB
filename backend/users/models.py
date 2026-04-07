from django.db import models

class Follow(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    followers = models.ManyToManyField('auth.User', related_name='following')

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Additional fields here.
