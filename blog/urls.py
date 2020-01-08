from django.urls import path
from blog import views

urlpatterns = [
    path('api/posts/', views.PostList.as_view(), name='posts-list'),
    path('api/post/<str:slug>/', views.PostDetail.as_view(), name='post-detail'),
    path('api/categories/', views.CategoryList.as_view(), name='categories-list'),
    path('api/category/<str:slug>/', views.CategoryDetail.as_view(), name='category-detail'),
]