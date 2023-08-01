import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from appCategory.models import *
from embed_video.fields import EmbedVideoField
from django.db.models.signals import pre_save
from django.dispatch import receiver

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class SeriesVideo(models.Model):
    title = models.CharField(("Dizi Adı"), max_length=50,null=True)
    url = EmbedVideoField(null=True)
    sezon = models.CharField(("Sezon"), max_length=50)
    bölüm = models.CharField(("Bölüm"), max_length=50)
    def __str__(self):
        return self.title

class MoviesVideo(models.Model):
    title = models.CharField(("Film Adı"), max_length=50,null=True)
    url = EmbedVideoField(null=True)
    def __str__(self):
        return self.title

#Film işaretcileri
class MovieMaker(models.Model):
    title = models.CharField(("Başlığı"), max_length=50,blank=True,null=True)
    text = models.TextField(("Açıklaması"),max_length=250,blank=True,null=True)
    image = models.ImageField(("Sembol"), upload_to=None,blank=True,null=True)

    def __str__(self):
        return self.title     
# FİLM CLASS
class Movie(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Film Adı"), max_length=50)
    text = models.TextField(("Film Açıklama"), max_length=500, blank=True)
    image = models.ImageField(("Film Resim"), upload_to=None, blank=True, null=True)
    yil = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ManyToManyField(Subcategory, verbose_name=("Alt Category"), blank=True)
    cast = models.TextField(("Oyuncular"), max_length=500, blank=True)
    director = models.CharField(("Yönetmen"), max_length=50, blank=True)
    writers = models.CharField(("Senarist"), max_length=50, blank=True)
    slug = models.SlugField(("Slug Film"), blank=True, null=True)
    moviemaker = models.ManyToManyField(MovieMaker, verbose_name=("İzleyici İşaretçileri"))
    fragman = models.FileField(("Frgaman"), upload_to=None, max_length=100, null=True)
    url = models.ForeignKey(MoviesVideo, verbose_name=("Film"), on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        super(Movie, self).save(*args, **kwargs)
        

    def __str__(self):
        return self.title 

# ********************
# DİZİ CLASS
class Series(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE,null=True)
    title=models.CharField(("Dizi Adı"), max_length=50)
    text=models.TextField(("Dizi Açıklama"),max_length=500)
    image=models.ImageField(("Dizi Resim"), upload_to=None,)
    category=models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
    subcategory=models.ManyToManyField(Subcategory, verbose_name=("Alt Category"),blank=True)
    year=models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    cast=models.TextField(("Oyuncular"),max_length=500)
    director=models.CharField(("Yönetmen"), max_length=50)
    writers=models.CharField(("Senarist"), max_length=50)
    slug=models.SlugField(("Slug Dizi"),blank=True,null=True)
    moviemaker=models.ManyToManyField(MovieMaker, verbose_name=("İzleyici İşaretçileri"),blank=True)
    fragman = models.FileField(("Frgaman"), upload_to=None, max_length=100,null=True)
    url = models.ManyToManyField(SeriesVideo, verbose_name=("Dizi"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Series, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name=("Film"),blank=True, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, verbose_name=("Dizi"),blank=True, on_delete=models.CASCADE)
    text = models.TextField(("Yorum"),max_length=800)
    date_now = models.DateTimeField(("Tarih ve Saat"), auto_now_add=True) 
    star = models.IntegerField(("Yorum Puanı"),default=5)




