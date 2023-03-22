from django.contrib import admin
from .models import Author, Book


admin.site.register(Author)
#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'author__name')

admin.site.register(Book, BookAdmin)