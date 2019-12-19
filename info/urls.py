from django.urls import path
from .views import Index, Participans, Locations, Blog
from .views import Gallery, Infrastructure, Contacts, Road

urlpatterns = [
    path('', Index.as_view(), name='index_url'),
    path('participants/', Participans.as_view(), name='participants_url'),
    path('locations/', Locations.as_view(), name='locations_url'),
    path('gallery/', Gallery.as_view(), name='gallery_url'),
    path('blog/', Blog.as_view(), name='blog_url'),
    path('road/', Road.as_view(), name='road_url'),
    path('infrastructure/', Infrastructure.as_view(), name='infrastructure_url'),
    path('contacts/', Contacts.as_view(), name='contacts_url'),
]