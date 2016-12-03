from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import image

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def add(request):
    data = request.GET['data']
    image=qrcode.make(data)



    return HttpResponse(image.show())






