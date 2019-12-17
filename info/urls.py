from django.urls import path
from .views import Index, Musicians, Scenes
from .views import Gallery, Blog, Location, Contacts

urlpatterns = [
    path('', Index.as_view(), name='index_url'),
    path('musicians/', Musicians.as_view(), name='musician_url'),
    path('scenes/', Scenes.as_view(), name='scene_url'),
    path('gallery/', Gallery.as_view(), name='gallery_url'),
    path('blog/', Blog.as_view(), name='blog_url'),
    path('location/', Location.as_view(), name='location_url'),
    path('contacts/', Contacts.as_view(), name='contacts_url'),
]