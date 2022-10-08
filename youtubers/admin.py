from django.contrib import admin
from .models import Youtuber


class YoutubersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'subs_count','price')
    search_fields = ('city','description','first_name', 'last_name')
    list_display_links = ('id', 'first_name')
    list_filter = ('city','category')

# Register your models here.
admin.site.register(Youtuber, YoutubersAdmin)