'''
Import the required packages
'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimononial

# Register your models here.


@admin.register(Testimononial)
class TestimonialAdmin(SummernoteModelAdmin):
    '''
    Posts the testimonials form
    '''
    list_display = ('name', 'title', 'content', 'created_on')
    search_fields = ['title', 'name', 'content']
    list_filter = ('approved', 'created_on')
    summernote_fields = ('content',)
    actions = ['approve_comments']

    # pylint: disable=unused-argument
    def approve_comments(self, request, queryset):
        '''
        Allows admin to select confirm from action drop down
        '''
        queryset.update(approved=True)
