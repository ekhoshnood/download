from django.contrib import admin
from .models import Post, Channel, Senf, SaleType, MyModelAdmin




admin.site.register(Senf)
admin.site.register(SaleType)
admin.site.register(Channel, MyModelAdmin)
admin.site.register(Post)
