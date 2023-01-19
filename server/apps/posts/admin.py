from django.contrib import admin

from server.apps.posts.models import Idea,Tool

# Register your models here.

admin.site.register(Idea)
admin.site.register(Tool)