from django.contrib import admin
from .models import Tag, Entry
# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created"]
    search_fields = ["title", "content"]
    list_filter = ["created", "tags"]
    ordering = ["-created"]

@admin.register(Tag)
class TagAdmon(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]