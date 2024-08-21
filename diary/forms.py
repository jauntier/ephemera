from django import forms
from .models import *

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'photo', 'video']

class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ['to_user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content_text', 'content_image']
        # widgets = {
        #     'content_text': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        # }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio']