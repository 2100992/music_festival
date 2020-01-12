from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


#     def dispatch(self, request, *args, **kwargs):
#         print(self.request.user.username)
#         if self.request.user.is_anonymous:
#             return HttpResponse('Залогинься')
#         else:
#             return super(PostList, self).dispatch(request, *args, **kwargs)


class PostList(APIView):
    permission_classes = [IsAuthenticated]

    posts = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        serializer = self.serializer_class(self.posts, many=True)
        user = request.user
        print()
        print(f'User username \n - {user.username}')
        print()
        print(f'Auth \n - {request.auth}')
        print()
        print('User groups:')
        for group in user.groups.all():
            print(f' - {group}')
        print()
        # print(dir(request))
        # print(dir(serializer))
        # serializer.data['user'] = request.user
        return Response(serializer.data)


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
