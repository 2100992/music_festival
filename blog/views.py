from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from rest_framework.decorators import api_view, permission_classes

from rest_framework import mixins


def print_user_info(request):
    print()
    print(f'User username \n - {request.user.username}')
    # print()
    # print(f'Auth \n - {request.auth}')
    print()
    print('User groups:')
    for group in request.user.groups.all():
        print(f' - {group}')
    print()
    # print(dir(request))
    # print(dir(serializer))
    # serializer.data['user'] = request.user


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        # IsAuthenticated,
    ]

    def perform_create(self, serializer):
        print_user_info(self.request)
        # print(f'dir(self.request.data = \n {dir(self.request.data)}')
        # serializer.is_valid
        # print(f'serializer.data = {serializer}')
        # category = Category.objects.
        serializer.save(author=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     self.serializer_class.author = self.request.user
    #     return super().create(request, *args, **kwargs)  

    # def dispatch(self, request, *args, **kwargs):
    #     print_user_info(self.request)
    #     # print()
    #     # print(f'Auth \n - {request.user.auth_token}')
    #     # if self.request.user.is_anonymous:
    #     #     return HttpResponse('Залогинься')
    #     # else:
    #     #     return super().dispatch(request, *args, **kwargs)
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print_user_info(self.request)
        return super().get(request, *args, **kwargs)


# class PostList2(
#         mixins.CreateModelMixin,
#         APIView
# ):

#     permission_classes = [
#         # IsAuthenticated,
#         AllowAny,
#     ]

#     posts = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request):
#         serializer = self.serializer_class(self.posts, many=True)
#         print_user_info(request)
#         return Response(serializer.data)

#     # def post(self, request):
#     #     # user = request.user
#     #     self.create(request)

#     #     # if request.auth:
#     #     #     self.create(request)

#     #     serializer = self.serializer_class(self.posts, many=True)
#     #     # user = request.user
#     #     # print_user_info(user)
#     #     return Response(serializer.data)

        # @api_view(['GET'])
        # # @permission_classes([IsAuthenticated])
        # def post_list(request, format=None):
        #     if request.method == 'GET':
        #         permission_classes = [IsAuthenticated]

        #         posts = Post.objects.all()

        #         serializer = PostSerializer(posts, many=True)

        #         user = request.user

        #         print()
        #         print(f'User username \n - {user.username}')
        #         print()
        #         print(f'Auth \n - {request.auth}')
        #         print()
        #         print('User groups:')
        #         for group in user.groups.all():
        #             print(f' - {group}')
        #         print()
        #         # print(dir(request))
        #         # print(dir(serializer))
        #         # serializer.data['user'] = request.user
        #         return Response(serializer.data)


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
