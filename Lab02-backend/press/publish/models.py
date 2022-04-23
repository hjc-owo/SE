from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    status_choice = (
        (0, "审核中"),
        (1, "已发布"),
        (2, "审核失败"),
    )
    status = models.SmallIntegerField(choices=status_choice, default=0)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
