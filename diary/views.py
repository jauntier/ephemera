from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Entry, Profile, FriendRequest
from .forms import EntryForm
from django.db.models import Q
from .utils import analyze_sentiment
from .forms import ProfileForm, EntryForm

def home(request):
    return render(request, 'diary/home.html')

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            sentiment = analyze_sentiment(entry.text)
            entry.mood = sentiment['compound']  # This can be refined further
            entry.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'diary/create_entry.html', {'form': form})

@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'diary/entry_list.html', {'entries': entries})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    sent_requests = FriendRequest.objects.filter(from_user=request.user, status='pending')
    received_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
    friends = profile.friends.all()

    return render(request, 'diary/profile.html', {
        'profile': profile,
        'sent_requests': sent_requests,
        'received_requests': received_requests,
        'friends': friends
    })




@login_required
def search_users(request):
    query = request.GET.get('q')
    results = []
    if query:
        # Ensure you are using the correct related name for the Profile model
        results = User.objects.filter(Q(username__icontains=query) | Q(profile__bio__icontains=query))
    return render(request, 'diary/search_results.html', {'results': results})

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    if not FriendRequest.objects.filter(from_user=request.user, to_user=to_user).exists():
        friend_request = FriendRequest.objects.create(from_user=request.user, to_user=to_user)
        print(f"Friend request created: {friend_request}")
    else:
        print(f"Friend request already exists between {request.user} and {to_user}")
    return redirect('profile_view')


@login_required
def accept_friend_request(request, user_id):
    friend_request = get_object_or_404(FriendRequest, from_user__id=user_id, to_user=request.user)
    if friend_request.to_user == request.user:
        friend_request.accept()
    return redirect('profile_view')


@login_required
def decline_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.to_user == request.user:
        friend_request.status = 'declined'
        friend_request.save()
    return redirect('profile_view')

@login_required
def friend_entries(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    if friend.profile in request.user.profile.friends.all():
        entries = Entry.objects.filter(user=friend).order_by('-created_at')
        print(f"User {request.user} is friends with {friend}")
        return render(request, 'diary/friend_entries.html', {'entries': entries, 'friend': friend})
    else:
        print(f"User {request.user} is NOT friends with {friend}")
        return redirect('profile_view')


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'diary/edit_profile.html', {'form': form, 'profile': profile})