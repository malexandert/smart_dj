"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views
import smart_dj.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', smart_dj.views.index, name='index'),
    url(r'^about/$', smart_dj.views.about, name='about'),
    url(r'^profile/$', smart_dj.views.profile, name='profile'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name':'smart_dj/login.html'}, name='login'),
    url(r'^logout$', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^register/$', smart_dj.views.register, name='register'),
    url(r'^make_room/$', smart_dj.views.make_room, name='make_room'),
    url(r'^join_room/$', smart_dj.views.join_room, name='join_room'),
    url(r'^add_song/$', smart_dj.views.add_song, name='add_song'),
    url(r'^room/(?P<pin>[a-zA-Z0-9_@\+\-]+)$', smart_dj.views.room, name='room')
]
