from django.contrib import admin
from django.utils.html import format_html

from .models import Slider,Team

# Register your models here.

class AdminSlider(admin.ModelAdmin):
    list_display = ('id','headline', 'subtitle','create_date')
    list_display_links = ('id', 'headline')
    search_fields= ('headline', 'subtitle')

class AdminTeam(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40">'.format(object.photo.url))

    list_display = ('id','myphoto', 'first_name', 'last_name', 'role')
    list_display_links = ('id','first_name')
    search_fields = ('first_name','last_name','role')
    list_filter = ('role',)



admin.site.register(Slider,AdminSlider)

admin.site.register(Team, AdminTeam)
