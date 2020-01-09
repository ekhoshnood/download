from django.shortcuts import render, get_object_or_404

from .defs import download_images
from .models import Post
import time

def download_btn(request):
    pk = download_images()
    i = get_object_or_404(Post, pk=pk)

    return render(request, 'result.html', {'image': i})


def delete_btn(request):
    print("in delete btn")
    i = get_object_or_404(Post, pk=1)



def homepage(request):
    return render(request, 'home.html')

