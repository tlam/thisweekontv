from calendar import Calendar
from datetime import date, timedelta

from django.shortcuts import render

from episodes.models import Episode
from shows.models import Show


def index(request):
    today = date.today()
    days = int(request.GET.get('days', 0))

    week = week_calendar(days)
    this_week = []
    for day in week:
        this_week.append({
            'day': day,
            'episodes': Episode.objects.filter(air_date=day),
        })

    if days:
        days += 7
    else:
        days = 7
        
    context = {
        'days': days,
        'shows': Show.objects.all(),
        'today': today,
        'this_week': this_week,
        'week': week,
    }
    return render(
        request,
        'index.html',
        context,
    )


def week_calendar(days):
    cal = Calendar(6)
    today = date.today() + timedelta(days=days)
    weeks = cal.monthdatescalendar(today.year, today.month)
    current_week = []
    for week in weeks:
        if week[0] <= today <= week[6]:
            current_week = week
            break

    return current_week
