from django.db import models
from django.conf import settings


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.comment


class Replies(models.Model):
    reply = models.TextField()
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    replier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.reply


class Tags(models.Model):
    post = models.ManyToManyField(Posts)
    tag = models.TextField()

    def __str__(self):
        return self.tag
