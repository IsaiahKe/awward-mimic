from django.contrib import admin
from .models import Profile,AppVote

# Register your models here.
admin.site.register(AppVote)
admin.site.register(Profile)