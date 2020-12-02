from django.urls import path

from crudApp import views

app_name = 'crudApp'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/<int:id>', views.detail, name="detail"),
    path('posts', views.posts, name="posts"),
    path('create', views.create, name="create"),
    path('store', views.store, name="store"),
    path('comments/store', views.comment_store, name="comment_store"),
    # ajax 예제
    path('posts-ajax/<int:id>', views.detail_ajax, name="detail_ajax"),
    path('comments/store-ajax', views.comment_store_ajax, name="comment_store_ajax"),
]