from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from posts.forms.forms import PostForm, UpdateForm
from posts.models.models import Post

check = False


def auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return False


def home_auth(request):
    if auth(request):
        return render(request, 'home.html')
    else:
        return render(request, 'auth.html')


class BrowserView(ListView):
    model = Post
    template_name = 'posts/browse.html'
    ordering = ['-published']

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'


class PostCreateView(CreateView):
    model = Post
    # form_class = PostForm
    template_name = 'posts/create_post.html'
    fields = ['title', 'author', 'description']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    fields = ['title', 'description']
    # form_class = UpdateForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = '/browse'
