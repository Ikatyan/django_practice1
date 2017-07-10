from django.contrib import admin
from .models import Book, BookInstance, Genre, Author


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['list_name', 'first_name', ('date_of_birth', 'date_of_death')]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Genre)
# admin.site.register(Author)
