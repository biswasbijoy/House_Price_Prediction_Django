from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from posts.models.categories import PostCategory
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(PostCategory, related_name='categories')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('posts:content', args=(str(self.pk)))


# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     body = models.TextField()
#     date_added = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return '%s - %s' % (self.post.title, self.name)
#
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.owner.username)
