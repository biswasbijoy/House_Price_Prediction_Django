from django.urls import path
from posts.views.views import *

app_name = 'posts'

urlpatterns = [
    path('browse', BrowserView.as_view(), name='browse'),
    path('content/<int:pk>', PostDetailsView.as_view(), name='content'),
    path('new-post/', PostCreateView.as_view(), name='new_post'),
    path('content/update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('content/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('filter', filter_posts, name='filter'),
    path('content/<int:pk>/comment/', CommentView.as_view(), name='comment'),
    path('content/<int:pk>/delete', CommentDeleteView.as_view(), name='deleteComment'),
    path('', home_auth, name='home'),
]
