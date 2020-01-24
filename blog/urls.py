from django.urls import path
from . import views

urlpatterns = [
    path('api/posts/', views.PostList.as_view(), name='posts-list'),
    # path('api/posts/', views.post_list, name='posts-list'),
    path('api/posts/<str:slug>/', views.PostDetail.as_view(), name='post-detail'),
    path('api/categories/', views.CategoryList.as_view(), name='categories-list'),
    path('api/categories/<str:slug>/', views.CategoryDetail.as_view(), name='category-detail'),
]