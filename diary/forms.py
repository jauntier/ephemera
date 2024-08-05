from django import forms
from .models import Entry, FriendRequest, User

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'photo', 'video', 'audio', 'mood', 'location', 'activity']

class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ['to_user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio']