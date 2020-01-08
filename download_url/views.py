from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .defs import download_images
from .models import Channels
import time

def download_btn(request):
    pk = download_images()
    print("after download images def")
    i = get_object_or_404(Channels, pk=pk)


    return render(request, 'result.html', {'image': i})
    # return render(request, 'result.html')


def delete_btn(request):
    print("in delete btn")
    i = get_object_or_404(Channels, pk=1)



def homepage(request):
    return render(request, 'home.html')