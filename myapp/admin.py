from django.contrib import admin
from .models import Post, User
# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'password']


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at', 'updated_at', 'user' ]
