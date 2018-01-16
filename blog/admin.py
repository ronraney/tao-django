from django.contrib import admin

from .models import Post, Writer, Translator, Book

@admin.register(Book)
#Define BookAdmin class

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'translator_note')
    fields = ['title', 'author', 'first_edition', 'translator_note', 'translators', 'summary', 'book_url']
    
@admin.register(Writer)
#Define WriterAdmin class

class WriterAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'year_of_birth', 'year_of_death', 'profile')
    fields = ['first_name', 'last_name', ('year_of_birth', 'year_of_death')]

@admin.register(Translator)
# Define the Translator class
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'year_of_birth', 'year_of_death', 'profile')
    fields = ['first_name', 'last_name', ('year_of_birth', 'year_of_death')] 
    
@admin.register(Post)
#  Define the Post class

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post Info', {
            'fields': ('title', 'author', 'created_date', 'published_date', 'thumbnail')
        }),
        ('Verse Section', {
            'fields': ('verse_title', 'verse', 'source', 'source_authors', 'source_translators')
        }),
        ('Commentary Section', {
            'fields': ('commentary_title', 'commentary'),
        }),
    )
    list_display = ('title', 'author', 'created_date', 'published_date')
