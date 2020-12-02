from multiprocessing import context

import json

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import RequestContext
from django.template.loader import get_template
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from crudApp.models import Post, Comment


# 기본 화면 (아무 기능 없음)
def home(request):
    return render(request, 'crudApp/home.html')


# 게시물 리스트 뷰
def posts(request):
    post_list = Post.objects.all()
    return render(request, 'crudApp/posts.html', context={'post_list': post_list})


# 게시물 상세보기 뷰
def detail(request, id):
    post = Post.objects.get(id=id)
    print(id)
    comment_list = Comment.objects.filter(post_id=post.id).all()
    return render(request, 'crudApp/detail.html', context={'post': post, 'comment_list': comment_list})


# 게시물 생성페이지 뷰
def create(request):
    return render(request, 'crudApp/create.html')


# 화면을 보여주는 뷰가 아닌, 데이터 저장을 위한 부분
def store(request):
    post = Post()  # post(테이블) 객체를 변수에 할당
    post.title = request.POST.get('title')
    post.writer = request.POST.get('writer')
    post.content = request.POST.get('content')
    post.save()  # post 테이블에 들어온 정보 저장

    return HttpResponseRedirect(reverse('crudApp:home'))


# 화면을 보여주는 뷰가 아닌, 댓글을 저장하기 위한 부분
def comment_store(request):
    comment = Comment()
    comment.post_id = request.POST.get('post_id')
    comment.content = request.POST.get('content')
    comment.save()

    return HttpResponseRedirect('/app/posts/'+request.POST.get('post_id'))


# 게시물 상세보기 뷰 (ajax 예제용)
def detail_ajax(request, id):
    post = Post.objects.get(id=id)
    print(id)
    comment_list = Comment.objects.filter(post_id=post.id).all()
    return render(request, 'crudApp/detail_ajax.html', context={'post': post, 'comment_list': comment_list})


# ajax 방식으로 반환값은 json 타입의 갑을 처리
@csrf_exempt
def comment_store_ajax(request):
    data = json.loads(request.body)
    print(data)
    comment = Comment()
    comment.post_id = data.get('post_id', None)
    comment.content = data.get('content', None)
    comment.save()

    comment_list = Comment.objects.filter(post_id=data.get('post_id', None)).all()
    data = serializers.serialize('json', comment_list)
    print(comment_list)
    return HttpResponse(data, content_type="application/json")

