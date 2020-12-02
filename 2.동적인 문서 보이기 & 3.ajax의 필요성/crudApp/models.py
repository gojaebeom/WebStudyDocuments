from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    writer = models.CharField(max_length=20, null=False)
    content = models.TextField(null=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 외래키 설정
    content = models.TextField(null=False)
