from django.contrib import admin
from .models import Post, Channel, Senf, SaleType


admin.site.register(Senf)
admin.site.register(SaleType)
admin.site.register(Channel)
admin.site.register(Post)
