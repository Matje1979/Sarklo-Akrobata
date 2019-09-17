from django.contrib import admin

# Register your models here.
from .models import Post, Oglas

# Register your models here.
admin.site.register(Post)
admin.site.register(Oglas)