from django.urls import path
from committee import views

urlpatterns = [
    path('', views.Index.as_view(), name='index_url'),
]