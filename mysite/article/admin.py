#Import packages needed for functionality
from django.contrib import admin
from .models import Post

#Setting admin view of the articles
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'tags')
    list_filter = ("status",)
    search_fields = ["title", "content", "tags"]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
