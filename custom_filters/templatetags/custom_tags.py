from django import template
from diary.models import FriendRequest

register = template.Library()

@register.filter
def has_sent_friend_request(user, target_user):
    return FriendRequest.objects.filter(from_user=user, to_user=target_user, status='pending').exists()

@register.filter
def has_received_friend_request(user, target_user):
    return FriendRequest.objects.filter(from_user=target_user, to_user=user, status='pending').exists()




