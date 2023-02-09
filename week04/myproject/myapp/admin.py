from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','status','title', 'author', 'published_date')
    list_display_links = ('id',)
    list_editable = ('title',)
    list_filter = ('author',)
    search_fields =('title',)
    actions = ['make_published','make_soldout']
    
    def make_published(self, request, queryset):
        queryset.update(status='published')
    
    def make_soldout(self, request, queryset):
        queryset.update(status='soldout')

admin.site.register(Book, BookAdmin)