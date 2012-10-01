from django.conf.urls import patterns, include, url

urlpatterns = patterns('shows.views',
    url(r'^(?P<show_id>\d+)/$', 'index', name='index'),
    url(r'^configuration/$', 'configuration', name='configuration'),
)
