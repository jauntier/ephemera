# from rest_framework import serializers
# from diary.models import User, Freelancer, Client
# from diary.models import Profile, Entry, Notification


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'

# class EntrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Entry
#         fields = '__all__'

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = '__all__'

from rest_framework import serializers
from diary.models import User, Profile, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['privacy', 'text', 'photo', 'video', 'audio', 'mood', 'location', 'activity', 'created_at']
