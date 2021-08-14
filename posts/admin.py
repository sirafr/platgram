"""POSTS ADMIN"""
# Django
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from posts.models import Post

# Registro de modelos
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """POST ADMIN"""
    list_display = ('pk','user','photo')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website')
    list_filter = ('created','modified',)
    

