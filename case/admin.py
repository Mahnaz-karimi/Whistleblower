from django.contrib import admin
from case.models import Case, Media, CaseInfo, Status

admin.site.register(Case)
admin.site.register(Media)
admin.site.register(CaseInfo)
admin.site.register(Status)

'''
for  filtering--- husk at informere navnet i admin register

class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'case_post')  # columnsname for at vises i table
    list_filter = ('case_post','title') # filter
    search_fields = ('title', 'description')  # søge resultalter from a column
    prepopulated_fields = {'description': ('title',)}  # all title saves in slug
    ordering = ['-title', '-case_post']  # sort some of columns efter hinanden!

    '''
