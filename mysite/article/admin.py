#Import packages needed for functionality
from django.contrib import admin
from .models import Post

#Setting admin view of the articles
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)
