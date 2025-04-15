from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_string

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

def get_random_file_path(instance, filename):
    filetype = filename.split(".")[-1]
    filename = get_random_string(10)
    return f"profile_pics/{filename}.{filetype}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to=get_random_file_path, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
