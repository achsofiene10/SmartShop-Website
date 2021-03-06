"""myproject URL Configuration

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
from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers
from webapp import views

router=routers.DefaultRouter()
router.register('clients',views.clientList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    url(r'^login/', views.login),
    url(r'^addimage/', views.AddImage),
    url(r'^recognize/', views.Recognize),
    url(r'^search/',views.searchimage),
    url(r'^cardnumber/', views.cardnumber),
    url(r'^userinfo/', views.userinfo),
    url(r'^createuser/', views.createuser),
    url(r'^deleteuser/(?P<email>.*)/$', views.deleteuser),
    url(r'^sendemail/', views.sendemail),
    url(r'^test/', views.test),

]
