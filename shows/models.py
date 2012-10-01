from datetime import datetime

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

    def __unicode__(self):
        return u'%s' % self.name

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
            Episode.objects.get_or_create(
                name=episode['EpisodeName'],
                show=self,
                number=int(episode['EpisodeNumber']),
                air_date=datetime.strptime(episode['FirstAired'], '%Y-%m-%d'),
            )
