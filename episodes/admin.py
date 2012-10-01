from django.contrib import admin

from episodes.models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('show', 'number', 'air_date', 'has_seen',)
    list_filter = ('show',)

admin.site.register(Episode, EpisodeAdmin)
