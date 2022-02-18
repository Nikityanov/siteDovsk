from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'anons', 'date')
    list_display_links = ('title', 'anons')
    search_fields = ('title', 'anons', 'text')


admin.site.register(Articles, ArticlesAdmin)
