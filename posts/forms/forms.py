from django import forms
from posts.models.models import Post, PostCategory

from django import forms
from posts.models.models import Post, PostCategory

choice_list = PostCategory.objects.all().values_list('category', 'category')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'visible'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
