# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-2-7

""" 定义 learning_logs 的 URL 模式 """
from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
