

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EntryViewSet, ProfileViewSet
# from rest_framework.authtoken.views import obtain_auth_token
# from . import views


# router = DefaultRouter()

# router.register(r'entries', EntryViewSet)
# router.register(r'profiles', ProfileViewSet)

# urlpatterns = [
    # path('create/', views.create_entry, name='create_entry'),
    # path('entries/', views.entry_list, name='entry_list'),
    # path('profile/', views.profile_view, name='profile_view'),
    # path('', views.home, name='home'),
#     path('api/', include(router.urls)),
#     path('api/auth/', obtain_auth_token, name='api_token_auth'),  # Token auth endpoint
# ]


from django.urls import path
from .views import UserSignupView, CustomAuthToken, LogoutView, ProfileView, EntryListCreateView, EntryDetailView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('entries/', EntryListCreateView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
]
