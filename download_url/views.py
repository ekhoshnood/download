from django.shortcuts import render, get_object_or_404, redirect

from .defs import download_images
from .models import Post
from .forms import Create_Post_form
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


# def create_post(request):
#
#     context = {}
#
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('must_authenticate')
#
#     form = Create_Post_form(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         #channel = TODO: get channel from valid user and set to channel because it is foriegn key
#         # obj.channel = channel
#         obj.save()
#         form = Create_Post_form()
#
#     context['form'] = form
#
#     return render(request, template_name=)


