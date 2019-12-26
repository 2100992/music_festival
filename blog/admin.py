from codecs import register
from django.contrib import admin

from django.contrib.auth.models import User
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
