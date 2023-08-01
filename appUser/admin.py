from django.contrib import admin
from django.contrib import admin
from .models import *

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display=('user','name','id')

@admin.register(PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=('user','id')

@admin.register(ProfilFoto)
class ProfilFoto(admin.ModelAdmin):
    list_display=('id',)

@admin.register(Mylist)
class Mylist(admin.ModelAdmin):
    list_display=('id','profil')

admin.site.register(Bildirim)
from .models import Notification


