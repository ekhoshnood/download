from django.contrib import admin
from .models import Post, Channel


admin.site.register(Channel)
admin.site.register(Post)
