# signals.py
"""Signal handlers for the relationship_app to manage UserProfile creation.
This module listens for the post_save signal of the User model to automatically create a UserProfile."""

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a UserProfile automatically when a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
