from django.contrib import admin

# Register your models here.
from .models import Youtuber
from django.utils.html import format_html

class YTAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="60" />'.format(object.photo.url))  # remember .url for photo 

    list_display=(

        'id',
        'myphoto',
        'name',
        'subs',
        'is_featured'

    )

    search_fields=(

        'name',
        'category',
        'camera'
    )
    list_filter=(
          'category',
        'camera',

    )
    list_display_links=(

        'id',
        'name'
    )

    list_editable=(
        'is_featured',
    )
admin.site.register(Youtuber,YTAdmin)
