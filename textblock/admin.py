from django.contrib import admin

from .models import TextBlock


class TextBlockAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', 'text')

    list_display = ('category', 'slug', 'title')


admin.site.register(TextBlock, TextBlockAdmin)
