from django import forms
from posts.models.models import Post
from posts.models.categories import PostCategory


class PostForm(forms.ModelForm):
    category = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PostCategory.CATEGORY_OPTION_CHOICES,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
