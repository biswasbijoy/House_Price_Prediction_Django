from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email')
        fields = ('first_name', 'last_name', 'email')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
        label="Old Password"  # Change the label for the old_password field
    )
    new_password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
        label="New Password"  # Change the label for the new_password1 field
    )
    new_password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
        label="Confirm Password"  # Change the label for the new_password2 field
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
