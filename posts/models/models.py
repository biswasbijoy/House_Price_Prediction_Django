from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from posts.models.categories import PostCategory


class Post(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)

    category = models.ManyToManyField(PostCategory, related_name='categories', blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('posts:content', args=(str(self.pk)))
