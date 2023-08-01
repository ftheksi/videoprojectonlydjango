from django.shortcuts import render
# import requests
import json


# class theMovieDb:
#     def __init__(self):
#         self.api_url = "https://api.themoviedb.org/3"
#         self.api_key = "1e6fe4edd28119f13e130989f784314a"
    

#     def getPopulers(self):
#         response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
#         print(response)
#         return response.json()
    
#     def getSearchMovies(self,keyword):
#         response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
#         return response.json()
    
# movieApi = theMovieDb()
# while True:
#     secim = input("1- Populer Movies\n2-Search Movies\n3- Exit\nSeçim: ")

#     if secim == "3":
#         break
#     else:
#         if secim == "1":
#             movies = movieApi.getPopulers()
#             for movie in movies["results"]:
#                 print(movie)
#         elif secim == "2":
#             keyword = input("keyword")
#             movies = movieApi.getSearchMovies(keyword)
#             for movie in movies["results"]:
#                 print(movie["name"])

# def video_view(request):
#     video = Video.objects.get(pk=1)  # Video modeline uygun şekilde veritabanından videoyu alın

#     context = {
#         'video': video,
#     }

#     return render(request, 'video.html', context)
