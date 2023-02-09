from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'published_date')
    list_display_links = ('id',)
    list_editable = ('title',)
    list_filter = ('author',)
    search_fields =('title',)

admin.site.register(Book, BookAdmin)