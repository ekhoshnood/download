from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .defs import download_images
from .models import Channels


def download_btn(request):
    download_images()
    print("after download images def")
    i = get_object_or_404(Channels, pk=1)
    return render(request, 'result.html', {'image': i})
    # return render(request, 'result.html')



def homepage(request):
    return render(request, 'home.html')