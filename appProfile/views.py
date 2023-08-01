from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification

# BİLDİRİM
def notifications(request):
    if request.method == "GET":
       notifications = Notification.objects.order_by('-tarih')[:5] # son 5 bildirim
       data = {
           'notifications': list(notifications.values('icerik','tarih'))
       }
       return JsonResponse(data)  

def notifications(request):
    if request.method == "GET":
       notifications = [
           {"icerik": "WEDNESDAY ÇIKIYOR", "tarih": "2023-05-17 10:00:00"},
           {"icerik": "HIZLI VE ÖFKELİ 9 GELİYOR", "tarih": "2023-05-17 11:00:00"},
           {"icerik": "İCERİK", "tarih": "2023-05-17 12:00:00"},
       ]
       data = {
           'notifications': notifications
       }
       return JsonResponse(data)

