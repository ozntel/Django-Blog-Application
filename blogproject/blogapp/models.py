from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    snippet = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    visible = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:PostDetailView', args=[self.pk])

class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=128)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    visible = models.BooleanField(default=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Comment from' + '|' + self.author
    class Meta:
        ordering = ['-pk']