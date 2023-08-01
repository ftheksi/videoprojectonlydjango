from django.db.models.signals import post_save, post_delete
from django.contrib import messages
from django.dispatch import receiver
from .models import *
from appMy.models import *
from django.contrib import messages
from appMy.views import index

from django.dispatch import Signal

notification_signal = Signal()

def NewBildirim(sender, instance, created, **kwargs):
    
    request = kwargs.get('request')
    if request is not None:
        if created == False:
            messages.info(f"This Topic: {instance} was updated")
        else:
            messages.info(f"This Topic: {instance} was created")


post_save.connect(NewBildirim, sender=Movie)


