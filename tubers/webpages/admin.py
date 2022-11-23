from django.contrib import admin
from django.utils.html import format_html

# customizing team info display 


class TeamAdmin(admin.ModelAdmin):
    #modifying a list
    def myphoto(self,object):
       return format_html('<img src="{}" width="40" />'.format(object.photo.url))  # remember .url for photo 

    # what all to display for a team member object
    list_display=('id','myphoto','firstname','lastname','created_date') 
    

    # making firstname clickable
    list_display_links=('firstname',)


# to bring a search filed 
    search_fields=('firstname',)


# to bring a filter filed 
    list_filter =('id',)


# Register your models here.
from .models import Slider,Team
admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)