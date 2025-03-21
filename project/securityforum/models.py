from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=22, unique=True, primary_key=True)

    def __str__(self):
        return f"username: {self.username}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"ID: {self.id}, author: {self.author}, header: '{self.header}', content: '{self.content}', pub_date: {self.pub_date.isoformat()}"
