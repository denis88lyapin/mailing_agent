from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'view_count', 'created_at')
    search_fields = ('title', 'body')
