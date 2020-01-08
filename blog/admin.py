from codecs import register
from django.contrib import admin

from django.contrib.auth.models import User
from blog.models import Post, Category

# Register your models here.


class PostInline(admin.TabularInline):
    model = Post.category.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [
    #     PostInline,
    # ]
    exclude = ('post',)
