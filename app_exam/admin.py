from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('question_text', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

# Register your models here.
