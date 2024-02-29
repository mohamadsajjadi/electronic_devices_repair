from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import render

from .models import MyUser
from payment.models import Wallet

# Create your views here.

@receiver(post_save, sender=MyUser) 
def created_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(person=instance)

@receiver(post_save, sender=MyUser) 
def save_wallet(sender, instance, **kwargs):
        instance.wallet.save()
