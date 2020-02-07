from django.shortcuts import render, get_object_or_404, redirect

from .defs import download_images
from .models import Post
from .forms import Channel_form
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


def create_post(request):
    form = Channel_form()
    if request.method == 'POST':
        form = Channel_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        context = {'form':form}
        return render(request, template_name="form.html", context=context)


