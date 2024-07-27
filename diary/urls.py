from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('entry_list/', views.entry_list, name='entry_list'),
    path('profile/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search_users/', views.search_users, name='search_users'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:user_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline_friend_request/<int:request_id>/', views.decline_friend_request, name='decline_friend_request'),
    path('friend_entries/<int:user_id>/', views.friend_entries, name='friend_entries'),
]
