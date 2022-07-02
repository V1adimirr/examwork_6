from django.contrib import admin

from guest_book.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['author', 'author_mail', 'status', 'created_at', 'updated_at']
    list_display_links = ['author']
    list_filter = ['created_at']
    search_fields = ['author', 'content']
    fields = ['author', 'author_mail', 'status', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Entry, EntryAdmin)
