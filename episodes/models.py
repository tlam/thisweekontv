from datetime import date, timedelta

from django.db import models


class Episode(models.Model):
    name = models.CharField(max_length=255)
    show = models.ForeignKey('shows.Show')
    number = models.IntegerField()
    air_date = models.DateField()
    has_seen = models.BooleanField()

    def __unicode__(self):
        return '%s: %i - %s' % (self.show, self.number, self.air_date)

    def description(self):
        return '%s, %i' % (self.show.name, self.number)

    def display_number(self):
        return (self.show.season * 100) + self.number

    def is_new(self):
        '''
        Check if episode is less than week old
        '''
        today = date.today()
        week = timedelta(7)
        day_zero = timedelta(0)
        delta = today - self.air_date
        return day_zero <= delta < week
