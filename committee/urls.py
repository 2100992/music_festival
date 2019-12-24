from django.urls import path
from committee import views

urlpatterns = [
    path('', views.Index.as_view(), name='committee_index_url'),
]