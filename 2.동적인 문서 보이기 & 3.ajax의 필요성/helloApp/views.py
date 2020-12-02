from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from helloApp.models import User


def index(request):
    user_list = User.objects.all()
    return render(request, 'helloApp/index.html', context={'user_list': user_list})


def show(request):
    return render(request, 'helloApp/index.html')


def create(request):

    return render(request, 'helloApp/create.html')


def store(request):
    if request.POST:
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.save()

    return HttpResponseRedirect(reverse('helloApp:index'))


def update(request):
    return render(request, 'helloApp/index.html')


def edit(request):
    return render(request, 'helloApp/index.html')


def destroy(request):
    return render(request, 'helloApp/index.html')
