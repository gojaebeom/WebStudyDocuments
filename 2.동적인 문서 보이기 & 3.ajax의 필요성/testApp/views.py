from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    name = "고재범"
    return HttpResponse("<h2>Hello, world."+name+" it is home")


def info(request):
    return HttpResponse("<html>"
                        "<head>"
                        "<title>HOME</title>"
                        "</head>"
                        "<body><h1>hello world!</h1></body>"
                        "</html>")


def create_post(request):
    return HttpResponse("<form action='/info' method='GET'>"
                        "<input name='id'><br>"
                        "<input name='name'><br>"
                        "<button type='submit'>생성</button>"
                        "</form>")


def user_info(request):
    user_id = request.GET.get('id')
    user_name = request.GET.get('name')
    return HttpResponse("<div>"
                        "<h2> 유저 정보 </h2>"
                        "<h4> 유저 번호 : "+ user_id +"</h4>"
                        "<h4> 유저 이름 : "+ user_name +"</h4>"
                        "</div>")
