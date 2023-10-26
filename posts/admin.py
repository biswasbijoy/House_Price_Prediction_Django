from django.contrib import admin
from posts.models.categories import PostCategory
from posts.models.models import Post, Comment

admin.site.register(PostCategory)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'published']
    list_filter = ['author', 'category']

