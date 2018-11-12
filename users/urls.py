#!/usr/bin/env python3
# coding=utf-8
# title          : urls.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/10/24 4:18
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from django.conf.urls import url
from django.contrib.auth.views import login as login_view
from users.views import logout_view,  register_view


urlpatterns = [
    url(r'^login/$', login_view, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    # url(r'register/$', register_view, name='register'),
]
