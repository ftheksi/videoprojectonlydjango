from django.db import models
from django.contrib.auth.models import User

 # BİLDİRİM 
class Notification(models.Model):
    icerik = models.CharField(max_length=255)
    tarih = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.icerik