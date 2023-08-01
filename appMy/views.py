from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User
from .models import *
from appUser.models import *
from appCategory.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.http import FileResponse
from django.views.decorators.cache import cache_control
from appUser.views import *
from appUser.signals import *
from django.db.models.signals import post_save, post_delete
from appMy.models import Movie
from django.dispatch import receiver
from appUser.models import Movie, Profil, Subcategory, Category, Mylist, SeriesVideo, MoviesVideo, Series

def indexPage(request):
    series = Series.objects.all()
    movies = Movie.objects.all()
    if request.user.is_authenticated:
        return redirect('ProfileUser')
    context={
        'series':series,
        'movies':movies,
    }
    return render(request, 'index.html',context)


def ContactUs(request, pid=None):
    profil = None
    if pid:
        profil = Profil.objects.get(id=pid)

    # if request.method == "POST":
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     title = request.POST["title"]
    #     text = request.POST["text"]

    #     contact = Contact(name=name,email=email,title=title,text=text)
    #     contact.save()
    #     return HttpResponseRedirect("/#contact")
    context = {
        "profil": profil,
    }
    return render(request, 'contact.html', context)

from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver

@login_required(login_url="/LoginUser/")
def index(request, pid, slug="all"):
    profil = Profil.objects.get(id=pid)
    subcategory = Subcategory.objects.all()
    categorys = Category.objects.all()
    mylist = Mylist.objects.filter(profil=profil)
    seriesvideo = SeriesVideo.objects.all()
    moviesvideo = MoviesVideo.objects.all()
    
    # varsayılan olarak her iki değişken 'None' atanır.
    movies, series = None, None
    
    if slug == 'all':
        movies = Movie.objects.all().order_by('-id')
        series = Series.objects.all().order_by('-id')
    elif slug == 'dizi':
        series = Series.objects.all().order_by('-id')
    elif slug == 'film':
        movies= Movie.objects.all().order_by('-id')

      
    context ={
         "title": "Anasayfa",
         "series": series,
         "movies": movies,
         'profil': profil,
         'subcategory': subcategory,
         'categorys': categorys,
         'mylist': mylist,
         'seriesvideo': seriesvideo,
         "moviesvideo":moviesvideo,
       }
    return render(request,'girisli_index.html',context)


@login_required(login_url="/LoginUser/")
def Dizindex(request, pid):
    profil = Profil.objects.get(id=pid)
    subcategory = list(Subcategory.objects.all())
    subcategory = random.sample(subcategory, 5)
    categorys = Category.objects.all()
    mylist = Mylist.objects.filter(profil=profil)
    seriesvideo = SeriesVideo.objects.all()
    moviesvideo = MoviesVideo.objects.all()
    series = Series.objects.all()

    if request.method == "POST" and request.POST.get('submit') == "myListSeries":
        movieid = request.POST.get('movieid')
        mylistem = Series.objects.get(id=movieid)
        mylistem = Mylist(profil=profil, series=mylistem)
        mylistem.save()

    context = {
        "title": "Anasayfa",
        "series": series,
        'profil': profil,
        'subcategory': subcategory,
        'categorys': categorys,
        'mylist': mylist,
        'seriesvideo': seriesvideo,
        'moviesvideo': moviesvideo,
    }
    return render(request, 'Dizi.html', context)

@login_required(login_url="/LoginUser/")
def Filmindex(request, pid):
    profil = Profil.objects.get(id=pid)
    subcategory = list(Subcategory.objects.all())
    subcategory = random.sample(subcategory, 5)
    categorys = Category.objects.all()
    mylist = Mylist.objects.filter(profil=profil)
    seriesvideo = SeriesVideo.objects.all()
    moviesvideo = MoviesVideo.objects.all()
    movies = Movie.objects.all()

    if request.method == "POST" and request.POST.get('submit') == "myListMovies":
        movieid = request.POST.get('movieid')
        mylistem = Movie.objects.get(id=movieid)
        mylistem = Mylist(profil=profil, movies=mylistem)
        mylistem.save()

    context = {
        "title": "Anasayfa",
        'profil': profil,
        'subcategory': subcategory,
        'categorys': categorys,
        'movies': movies,
        'mylist': mylist,
        'seriesvideo': seriesvideo,
        'moviesvideo': moviesvideo,
    }
    return render(request, 'Film.html', context)


def ContentDetail(request, pid, sid):
    profil = Profil.objects.get(id=pid)
    movies = Movie.objects.get(id=sid)
    categorys = Category.objects.all()
    video = MoviesVideo.objects.all()
    # dizi = Series.objects.get(id=uid)
    # comments = Comment.objects.filter(series=dizi).order_by("-star")
    # puan=0
    # if request.method == "POST":
    #     submit = request.POST.get("submit")
    #     if submit == "comment":
    #       text = request.POST.get("text")
    #       try:
    #             star = int(request.POST.get("star"))
    #       except:
    #             return redirect('/MovieX/'+ uid + '/ContentDetail')

    #       comment = Comment(user=request.user,series=dizi,text=text,star=star)
    #       comment.save()

    #       for i in comments:
    #            puan += i.star

    #       dizi.stars = round(puan/len(comments),1)
    #       dizi.save()
    #       return redirect('/Moviex/'+ uid + '/ContentDetail')
    context = {
        "movies": movies,
        "profil": profil,
        'categorys': categorys,
        'video':video,
    }
    return render(request, 'movie-detail.html', context)

def SeriesDetail(request, pid, sid):
    profil = Profil.objects.get(id=pid)
    series = Series.objects.get(id=sid)
    video = SeriesVideo.objects.all()
    categorys = Category.objects.all()
    # dizi = Series.objects.get(id=uid)
    # comments = Comment.objects.filter(series=dizi).order_by("-star")
    # puan=0
    # if request.method == "POST":
    #     submit = request.POST.get("submit")
    #     if submit == "comment":
    #       text = request.POST.get("text")
    #       try:
    #             star = int(request.POST.get("star"))
    #       except:
    #             return redirect('/MovieX/'+ uid + '/ContentDetail')

    #       comment = Comment(user=request.user,series=dizi,text=text,star=star)
    #       comment.save()

    #       for i in comments:
    #            puan += i.star

    #       dizi.stars = round(puan/len(comments),1)
    #       dizi.save()
    #       return redirect('/Moviex/'+ uid + '/ContentDetail')
    context = {
        "series": series,
        "profil": profil,
        'categorys': categorys,
        'video':video,
    }
    return render(request, 'series-detail.html', context)


def searchMovies(request,pid):
    profil = Profil.objects.get(id=pid)
    subcategory = Subcategory.objects.all()
    if 'q' in request.GET and request.GET['q'] != "":
        print("Burada",request.GET)
        q = request.GET['q']
        series = Series.objects.filter(title__icontains=q)
        print(series)
        movies = Movie.objects.filter(title__icontains=q)
        print(movies)
    else:
        return redirect('girisli_index.html')
    return render(request, 'girisli_index.html', {
            'series': series,
            'profil': profil,
            'movies': movies,
            'subcategory':subcategory,
            })



def SssPage(request, pid=None):
    profil = None
    if pid:
        profil = Profil.objects.get(id=pid)

    context = {
        "profil": profil,
    }
    return render(request, 'sss.html', context)

def WatchMovie(request,mid,pid):
    profil = Profil.objects.get(id=pid)
    video = MoviesVideo.objects.get(id=mid)

    context={
        "video":video,
        'profil':profil,
    }
    return render(request,'watch-movie.html',context)



@cache_control(max_age=3600)  # 1 saat önbelleğe alma süresi
def WatchSeries(request, mid, pid):
    profil = Profil.objects.get(id=pid) 
    videos = SeriesVideo.objects.get(id=mid)
    context = {
        "videos": videos,
        "profil": profil,
    }
    
    return render(request, 'watch-series.html', context)




