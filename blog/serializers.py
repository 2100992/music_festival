from .models import Post, Category

from rest_framework import serializers

from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class CategorySerializer(serializers.ModelSerializer):

    post = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug',
    )

    class Meta:
        model = Category
        fields = [
            'title',
            'post',
            'slug'
        ]
        read_only_fields = [
            'slug',
        ]


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(required=False, read_only=True,)

    category = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'slug',
            'status',
            'category',
            'markdown_field',
            'html_field',
            'convetr_md_to_html',


        ]
        read_only_fields = [
            'slug',
            'updated',
            'publication_date',

        ]

