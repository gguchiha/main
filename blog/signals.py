from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Edit_Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
    if created:
        Edit_Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwards):
    instance.edit_profile.save()