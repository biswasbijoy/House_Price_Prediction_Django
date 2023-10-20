from django.urls import path
from posts.views.views import *

app_name = 'posts'

urlpatterns = [
    path('browse', BrowserView.as_view(), name = 'browse'),
    path('content/<int:pk>', PostDetailsView.as_view(), name = 'content'),
    path('new-post/', PostCreateView.as_view(), name = 'new_post'),
    path('content/update/<int:pk>', PostUpdateView.as_view(), name = 'update_post'),
    path('content/delete/<int:pk>', PostDeleteView.as_view(), name = 'delete_post'),
    path('home', home_auth, name = 'home'),
]