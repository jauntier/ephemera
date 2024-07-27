# from rest_framework import generics
# from django.shortcuts import render, redirect
# from rest_framework.authtoken.models import Token
# from diary.forms import EntryForm
# from diary.models import Entry, Profile
# from diary.utils import analyze_sentiment
# from django.contrib.auth.decorators import login_required
# from rest_framework import viewsets
# from .serializers import FreelanceSignupSerializer, UserSerializer, ClientSignupSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# import logging
# from django.db import transaction
# logger = logging.getLogger(__name__)

# def home(request):
#     return render(request, 'diary/home.html')

# @login_required
# def create_entry(request):
#     if request.method == 'POST':
#         form = EntryForm(request.POST, request.FILES)
#         if form.is_valid():
#             entry = form.save(commit=False)
#             entry.user = request.user
#             sentiment = analyze_sentiment(entry.text)
#             entry.mood = sentiment['compound']
#             entry.save()
#             return redirect('entry_list')
#     else:
#         form = EntryForm()
#     return render(request, 'diary/create_entry.html', {'form': form})

# @login_required
# def entry_list(request):
#     entries = Entry.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'diary/entry_list.html', {'entries': entries})

# @login_required
# def profile_view(request):
#     profile, created = Profile.objects.get_or_create(user=request.user)
#     return render(request, 'diary/profile.html', {'profile': profile})


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

# class EntryViewSet(viewsets.ModelViewSet):
#     queryset = Entry.objects.all()
#     serializer_class = EntrySerializer
#     permission_classes = [IsAuthenticated]


from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSignupSerializer, UserSerializer, ProfileSerializer, EntrySerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from diary.models import Entry

class UserSignupView(generics.GenericAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "Account created successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

class EntryListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)
