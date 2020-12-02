from django.urls import path

from helloApp import views

app_name = 'helloApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('store', views.store, name="store"),
    path('update', views.update, name="update"),
    path('<int:id>', views.show, name="show"),
]
