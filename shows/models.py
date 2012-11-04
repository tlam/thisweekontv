from datetime import date, datetime

from django.core.urlresolvers import reverse
from django.db import models
from lxml import etree
import requests

from episodes.models import Episode
from home.models import TVConfiguration


class Show(models.Model):
    name = models.CharField(max_length=100)
    tvdb_id = models.IntegerField()
    season = models.IntegerField()
    last_seen = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % self.name

    def to_watch(self):
        return self.episode_set.filter(has_seen=False, air_date__lte=date.today())

    def refresh(self):
        api_key = TVConfiguration.objects.get().api_key
        url = 'http://www.thetvdb.com/api/%s/series/%i/all/en.xml' % (api_key, self.tvdb_id)

        xml = requests.get(url).content
        tree = etree.fromstring(xml)
        #tree = etree.parse('shows/fixtures/how.xml')
        seasons = {}
        for episode in tree.findall('Episode'):
            print dir(episode)
            episode_dict = {}
            for item in episode.getchildren():
                episode_dict[item.tag] = item.text
            season = episode_dict['SeasonNumber']
            if season in seasons:
                seasons[season].append(episode_dict)
            else:
                seasons[season] = [episode_dict]

        current_season = str(self.season)
        for episode in seasons[current_season]:
            episode_name = episode['EpisodeName']
            first_aired = episode['FirstAired']
            if not all([episode_name, first_aired]):
                continue
            defaults = {
                'name': episode_name,
                'air_date': datetime.strptime(first_aired, '%Y-%m-%d'),
            }
            obj, created = Episode.objects.get_or_create(
                number=int(episode['EpisodeNumber']),
                show=self,
                defaults=defaults,
            )

            if not created:
                obj.name = defaults['name']
                obj.air_date = defaults['air_date']
                obj.save()
