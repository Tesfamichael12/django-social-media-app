from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'user__username')
    date_hierarchy = 'created_at'