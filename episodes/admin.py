from django.contrib import admin

from episodes.models import Episode


def mark_as_seen(modeladmin, request, queryset):
    queryset.update(has_seen=True)
mark_as_seen.short_description = 'Mark selected episodes as seen'

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('show', 'number', 'air_date', 'has_seen',)
    list_filter = ('show',)
    actions = [mark_as_seen]

admin.site.register(Episode, EpisodeAdmin)
