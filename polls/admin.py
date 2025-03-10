from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]

    # fieldsets = [
    #     (None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"]}),
    # ]

    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]

# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
