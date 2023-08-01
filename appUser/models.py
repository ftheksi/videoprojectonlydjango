from django.db import models
from django.contrib.auth.models import User
from appMy.models import *
# from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
# from creditcards import types

# profil-edit select
SPECTATOR = (
    ('Genel izleyici', 'Genel izleyici'),
    ('7+', '7+'),
    ('13+', '13+'),
    ('18+', '18+'),
)

LANGUAGE = (
    ('Türkçe', 'Türkçe'),
    ('English', 'English'),
)

# assert types.get_type('4444333322221111') == types.CC_TYPE_VISA
# assert types.get_type('343434343434343') == types.CC_TYPE_AMEX
# assert types.get_type('0000000000000000') == types.CC_TYPE_GENERIC

class PackageType(models.Model):
    title= models.CharField(("Paket Adı"),max_length=50, null=True)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    tel = models.CharField(max_length=12)
    password=models.CharField(("Password"), max_length=50,default="-")
    dogum_tarihi= models.DateField(("Doğum Tarihi"),blank=True,null=True)
    package=models.ForeignKey(PackageType, verbose_name=("Paket Bilgisi"), on_delete=models.CASCADE,blank=True,null=True)
    
#     credit_card=


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    name = models.CharField(("Profil Adı"), max_length=50,blank=True,)
    image = models.FileField(("Profil Fotoğrafı"), upload_to='', max_length=100)
    spectator=models.CharField(("İzleyici Kitlesi"), max_length=50, choices=SPECTATOR, null=True)
    language=models.CharField(("Dil Seçimi"), max_length=50, choices=LANGUAGE, null=True)
    def __str__(self):
        return self.name

class ProfilFoto(models.Model):
    image = models.FileField(("Profil Fotoğrafı"), upload_to='', max_length=100)

class Mylist(models.Model):
    profil=models.ForeignKey(Profil, verbose_name=("Profil"), on_delete=models.CASCADE)
    movies= models.ForeignKey(Movie, verbose_name=("Filmler"), on_delete=models.CASCADE, null=True)
    series=models.ForeignKey(Series, verbose_name=("Diziler"), on_delete=models.CASCADE, null=True)

class Bildirim(models.Model):
    name = models.CharField(("Name"), max_length=50)
    description = models.TextField(("Açıklama"), max_length=500)

# class CreditCard(models.Model):
#     cc_number = CardNumberField(('Kart Numarası'))
#     cc_date = CardExpiryField(('Son Kullanma Tarihi'))
#     cc_code = SecurityCodeField(('Güvenlik Kodu'))

# class Film (models.Model):
#     adi = models.CharField(max_length=100)

#     @classmethod
#     def add_film(cls, film_adi):
#         film = cls(adi=film_adi)
#         film.save()
#         return film
    
#     def __str__(self):
#         return self.adi

# class Contact(models.Model):
#     name = models.CharField(("İsim"), max_length=50)
#     email = models.EmailField(("Email"), max_length=254)
#     title = models.CharField(("Konu"), max_length=50)
#     text = models.TextField(("Mesaj"), max_length=500)
    
#     def __str__(self):
#         return self.name
from django.db import models
class Notification(models.Model):
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return self.message[:50]




    

