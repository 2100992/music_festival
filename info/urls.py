from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index_url'),
    path(
        'login/',
        views.LoginViewClass.as_view(),
        name='login_url'
    ),
    path(
        'signup/',
        views.SignupViewClass.as_view(),
        name='sungup_url'
    ),
    path('participants/', views.Participans.as_view(), name='participants_url'),
    path('locations/', views.Locations.as_view(), name='locations_url'),
    path('gallery/', views.Gallery.as_view(), name='gallery_url'),
    path('blog/posts/', views.BlogPosts.as_view(), name='blog_posts_url'),
    path('blog/post/<str:slug>/', views.BlogPostDetail.as_view(),
         name='blog_post_detail_url'),
    path('blog/categories/', views.BlogCategories.as_view(),
         name='blog_categories_url'),
    path('blog/category/<str:slug>/', views.BlogCategoryDetail.as_view(),
         name='blog_category_detail_url'),
    path('road/', views.Road.as_view(), name='road_url'),
    path('infrastructure/', views.Infrastructure.as_view(),
         name='infrastructure_url'),
    path('contacts/', views.Contacts.as_view(), name='contacts_url'),
    path('prof-redirect/', views.profile_redirect, name='profile_redirect_url'),
    path('small-test/', views.SmallTest.as_view(), name='small_test'),
]
