"""
URL configuration for lifebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),  # Assuming allauth is being used
#     path('diary/', include('diary.urls')),  # Include the URLs from the diary app
#     path('create/', include('diary.urls')),  # Ensure this is correct if 'create' is part of diary
#     path('entries/', include('diary.urls')),  # Ensure this is correct if 'entries' is part of diary
#     path('profile/', include('diary.urls')),  # Ensure this is correct if 'profile' is part of diary
# ]


from django.contrib import admin
from django.urls import path, include
from diary import views as diary_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', diary_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('diary/', include('diary.urls')),
    path('', include('diary.urls')),
]


urlpatterns += staticfiles_urlpatterns()