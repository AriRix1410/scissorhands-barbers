from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimononial

# Register your models here.


@admin.register(Testimononial)
class TestimonialAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_on')
    search_fields = ['title', 'name', 'content']
    list_filter = ('approved', 'created_on')
    summernote_fields = ('content',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
