"""leaderboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.urls import path, re_path
from competition.views import *
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',home,name="home"),
#     path('team/new',createTeamView.as_view(), name='newteam'),
#     re_path('team/(?P<pk>\d+)',teamDetail,name='team-detail'),
#     path('match/new',createMatch, name='newmatch'),
#     re_path('leaderboard/(?P<type>\w+)',showLeaderboard,name='leaderboard')
# ]

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home', home, name="home"),
    url(r'team/new', createTeamView.as_view(), name='newteam'),
    url(r'player/new', createPlayerView.as_view(), name='newplayer'),
    url('leaderboard/(?P<type>\w+)', showLeaderboard, name='leaderboard'),
    url('match/new', createMatch, name='newmatch'),
    url('team/(?P<pk>\d+)', teamDetail, name='team-detail'),
]
