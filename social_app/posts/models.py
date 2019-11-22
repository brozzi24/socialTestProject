from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=datetime.now)

    # To order the post by newest first
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        name = "{} {}".format(self.id, self.author)
        return name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        name = "{} {}".format(self.id, self.author)
        return name
