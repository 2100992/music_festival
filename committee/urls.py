from django.urls import path
from . import views

app_name = 'committee' 

urlpatterns = [
    path('', views.Index.as_view(),
         name='index'),
    path('applicant/', views.ApplicantView.as_view(),
         name='applicant_url'),
    path('committeeman/', views.CommitteemanView.as_view(),
         name='committeeman_url'),
]
