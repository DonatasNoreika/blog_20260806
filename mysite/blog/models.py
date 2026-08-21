from django.contrib.auth.models import User, AbstractUser
from django.db import models
from tinymce.models import HTMLField


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profile_pics", null=True, blank=True)


class Post(models.Model):
    title = models.CharField()
    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to='blog.CustomUser', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="covers", null=True, blank=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(to="Post",
                             on_delete=models.CASCADE,
                             related_name="comments")
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to='blog.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
