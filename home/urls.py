"""choonbom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
# from . import views
from django.conf.urls import url, include
from home import views
from django.contrib.auth.views import LogoutView


# app_name = 'home'
urlpatterns = [
    path('', views.main, name='main'),
    # path('<int:uid>/', views.signcomplete, name='signcomplete'),
    # path('test/', views.test, name='test'),
    path('accounts/', include('allauth.urls')),
    # path('choosePartner/', views.choosePartner, name='choosePartner'),
    path('<int:uid>/myinfo/', views.myinfo, name='myinfo'),
    path('<int:uid>/choosePartner/', views.choosePartner, name='choosePartner'),
    path('<int:uid>/choosePlace/', views.choosePlace, name='choosePlace'),
    path('<int:uid>/chooseFamily/', views.chooseFamily, name='chooseFamily'),

    # path('accounts/logout/', views.logout, name='logout'),
    path('logout/', LogoutView.as_view()),
    # path('logout/', views.logout, name='logout'),
    
    # path('accounts/logout/', views.logout, name='logout'),
    # url(r'^$', views.index, name='index'),
    # url(r'', include('home.urls')),
    # path('', include('home.urls'))
]
