from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from posts.forms.forms import PostForm, UpdateForm, CommentForm
from posts.models.categories import PostCategory
from posts.models.models import Post, Comment

check = False


def auth(request):
    if request.user.is_authenticated:
        return True
    else:
        return False


@login_required(login_url='/login')
def home_auth(request):
    return render(request, 'starting.html')


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
    form_class = PostForm
    template_name = 'posts/create_post.html'
    # fields = ['title', 'author', 'description', 'category']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    # fields = ['title', 'description', 'category']
    form_class = UpdateForm


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = '/browse'


def filter_posts(request):
    if request.method == 'GET':
        selected_categories = request.GET.getlist('categories')

        # Fetch all category choices
        category_choices = PostCategory.CATEGORY_OPTION_CHOICES

        if selected_categories:
            posts = Post.objects.filter(category__in=selected_categories)
        else:
            posts = Post.objects.all()

        context = {
            'object_list': posts,
            'category_choices': category_choices,
            'selected_categories': selected_categories,  # Pass selected categories to the context
        }

        return render(request, 'posts/browse.html', context)


# class CommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     # fields = '__all__'
#     template_name = 'posts/comment.html'
#
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)
#
#     success_url = reverse_lazy('posts:browse')
class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Set the comment owner to the current user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:content', args=[self.kwargs['pk']])


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/delete_comment.html'
    success_url = '/browse'
