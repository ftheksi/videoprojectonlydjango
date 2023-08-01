from django.contrib import admin
from .models import *
from django.contrib import messages
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=('title','slug','category')

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display=('title','slug',)

@admin.register(MovieMaker)
class MovieMakerAdmin(admin.ModelAdmin):
    list_display=('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('user','movie','series','text','date_now','star')

@admin.register(MoviesVideo)
class CommentAdmin(admin.ModelAdmin):
    list_display=('title','url')

@admin.register(SeriesVideo)
class CommentAdmin(admin.ModelAdmin):
    list_display=('title','bölüm','sezon')




