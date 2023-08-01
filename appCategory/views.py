from django.shortcuts import render
from .models import *
# Create your views here.

# Dizi-Film kategori
def contentCategory(request):
    contentcategory = Category.objects.all()


    context={
        'contentcategory':contentcategory

    }
    return render(request,'user/girisli_index.html',context)

