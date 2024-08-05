from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Entry)

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follower)
# admin.site.register(Entry)