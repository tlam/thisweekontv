from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls', namespace='home'), name='home'),
    url(r'^shows/', include('shows.urls', namespace='shows'), name='shows'),

    url(r'^admin/', include(admin.site.urls)),
)
