from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")
