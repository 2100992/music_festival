from django.urls import path
from timetable import views


urlpatterns = [
    path('', views.Index.as_view(), name='timetable_index_url'),
]