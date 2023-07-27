from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'body', 'created', 'updated', 'active']
    list_filter = ['active, created, updated']