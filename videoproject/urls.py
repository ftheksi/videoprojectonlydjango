from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *
from appUser.views import *
from appProfile.views import *
from appUser.views import activate_account
from appVideo.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('Moviex/<pid>/category/all/', index, name="index"),
    path('Moviex/<pid>/Dizi', Dizindex, name="Dizindex"),
    path('Moviex/<pid>/Film', Filmindex, name="Filmindex"),
    path('Moviex/<pid>/ContentDetail/<sid>',ContentDetail, name='ContentDetail'),
    path('Moviex/<pid>/category/all/', index, name="index"),
    path('Moviex/<pid>/category/<slug>/', index, name="index"),
     path('Moviex/<pid>/SeriesDetail/<sid>',SeriesDetail, name='SeriesDetail'),
    path('Moviex/<pid>/ContentDetail/<sid>', ContentDetail, name='ContentDetail'),
    path('Moviex/<pid>/ContentDetail/', ContentDetail, name='ContentDetail'),
    path('<pid>/ContactUs/', ContactUs, name="ContactUswithpid"),
    path('ContactUs/', ContactUs, name="ContactUs"),
    path('<pid>/Sss/', SssPage, name='SssPagewithpid'),
    path('Sss/', SssPage, name='SssPage'),
    path('Moviex/<pid>/WatchMovie/<mid>', WatchMovie, name='WatchMovie'),
    path('Moviex/<pid>/WatchSeries/<mid>', WatchSeries, name='WatchSeries'),
    # USER
    path('LoginUser/', LoginUser, name="LoginUser"),
    path('logout/', LogoutUser, name="LogoutUser"),
    path('RegisterUser/', RegisterUser, name="RegisterUser"),
    path('ProfileEdit/<pid>', ProfileEdit, name="ProfileEdit"),
    path('ProfileUser/', ProfileUser, name="ProfileUser"),
    path('ProfileDel/<pid>', ProfileDel, name="ProfileDel"),
    path('Account/<pid>', Account, name="Account"),
    path('AddList/<pid>', AddList, name="AddList"),
    path('ListDel/<pid>', ListDel, name="ListDel"),
    path('sifreunutma/', sendMail, name='sifreunutma'),
    path('activate/<str:uidb64>/<str:token>/',
         activate_account, name='activate_account'),
    path('UserDelete/<id>', UserDelete, name='UserDelete'),
    path('notifications', notifications, name="notifications"),
    path('searchMovies/<pid>', searchMovies, name="searchMovies"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
