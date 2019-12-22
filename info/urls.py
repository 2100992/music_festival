from django.urls import path
from info import views

urlpatterns = [
    path('', views.Index.as_view(), name='index_url'),
    path('participants/', views.Participans.as_view(), name='participants_url'),
    path('locations/', views.Locations.as_view(), name='locations_url'),
    path('gallery/', views.Gallery.as_view(), name='gallery_url'),
    path('blog/', views.Blog.as_view(), name='blog_url'),
    path('road/', views.Road.as_view(), name='road_url'),
    path('infrastructure/', views.Infrastructure.as_view(), name='infrastructure_url'),
    path('contacts/', views.Contacts.as_view(), name='contacts_url'),
    path('prof-redirect/', views.profile_redirect, name='profile_redirect_url'),
]