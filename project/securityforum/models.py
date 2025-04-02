from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published", default=datetime.now)

    def __str__(self):
        return f"ID: {self.id}, author: {self.author}, header: '{self.header}', content: '{self.content}', pub_date: {self.pub_date.isoformat()}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published", default=datetime.now)

    def __str__(self):
        return f"author: {self.author.id}, content: {self.content}, pub_date: {self.pub_date.isoformat()}"
