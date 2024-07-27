from django import forms
from .models import Entry, Profile, FriendRequest

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
        model = Profile
        fields = ['bio']
