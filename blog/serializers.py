from blog.models import Post, Category

from rest_framework import serializers

from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryser=Post.objects.all())

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
        slug_field='slug'
    )

    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'post',

        ]
    
    # def create


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(required=False, read_only=True,)
    # author = serializers.PrimaryKeyRelatedField(
    #     many=False,
    #     read_only=True,
    #     # queryset=User.objects.all()
    # )

    # category = CategorySerializer(required=False, read_only=True,)
    category = serializers.SlugRelatedField(
        many=True,
        # read_only=True,
        slug_field='slug',
        queryset=Category.objects.all()
    )

    # category = CategorySerializer(required=False, queryset=Category.objects.all())


    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'title',
            'slug',
            'status',
            'markdown_field',
            'html_field',
            'updated',
            'publication_date',
            'category',
            'author',
        ]


# class PostLinkSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
