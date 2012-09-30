from django.db import models


class TVConfiguration(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name
