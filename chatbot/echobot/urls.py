# -*- coding:utf-8 -*-


from django.conf.urls import url

from chatbot.echobot import views

urlpatterns = [
    url(r"^$", views.index),
    url(r'^callback/', views.callback),
]
