from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField()
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        textDate = str(self.created.strftime("%b. %d, %Y, %I:%M %p"))
        name = "{} {}".format(self.author, textDate)
        return name