# from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

# from rest_framework.decorators import api_view, permission_classes

# from rest_framework import mixins

'''experimental function for testing authorization settings'''
def print_user_info(request):
    print()
    print(f'User username \n - {request.user.username}')
    print()
    print('User groups:')
    for group in request.user.groups.all():
        print(f' - {group}')
    print()



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    '''can be used - settings - 'DEFAULT_PERMISSION_CLASSES': (),'''
    # permission_classes = [
    #     IsAuthenticatedOrReadOnly,
    #     # IsAuthenticated,
    # ]

    '''automatic task of the author of the post'''
    def perform_create(self, serializer):
        # print_user_info(self.request)
        serializer.save(author=self.request.user)

    '''experimental editing of a method for testing authorization settings'''
    # def get(self, request, *args, **kwargs):
    #     print_user_info(self.request)
    #     return super().get(request, *args, **kwargs)



class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [
    #     IsAuthenticatedOrReadOnly,
    #     # IsAuthenticated,
    # ]


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
