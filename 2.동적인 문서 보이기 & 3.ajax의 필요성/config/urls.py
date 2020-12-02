from django.urls import path
from django.urls import include
urlpatterns = [
    path('', include('testApp.urls')),
    path('app/', include('crudApp.urls')),
    path('hello/', include('helloApp.urls')),
]
