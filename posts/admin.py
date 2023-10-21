from django.contrib import admin

from posts.models.categories import PostCategory
from posts.models.models import Post

admin.site.register(PostCategory)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'description', 'published']
    list_filter = ['author', 'category']
