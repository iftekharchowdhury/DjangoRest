from django.contrib import admin
from .models import Snippet
# Register your models here.

class SnippetUser(admin.ModelAdmin):
    list_display = ('owner', 'created', 'title', 'code')

admin.site.register(Snippet, SnippetUser)
