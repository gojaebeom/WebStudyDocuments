from django.urls import path

from testApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create_post, name="create"),
    path('info', views.user_info, name="info"),
]