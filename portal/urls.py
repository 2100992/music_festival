"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from allauth.account.views import login, logout

from info.urls import urlpatterns as info_urls


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'allauth-login/',
        login,
        name='allauth-login_url'
    ),
    path(
        'allauth-logout/',
        logout,
        name='allauth-logout_url'
    ),

    path(
        'accounts/',
        include('allauth.urls')
    ),
    path(
        'auth/',
        include('djoser.urls')
    ),
    path(
        'auth/',
        include('djoser.urls.authtoken')
    ),
    path(
        'auth/',
        include('djoser.urls.jwt')
    ),



    path(
        'committee/',
        include('committee.urls')
    ),
    path(
        'timetable/',
        include('timetable.urls')
    ),
    path(
        'blog/',
        include('blog.urls')
    ),

]

urlpatterns += info_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
