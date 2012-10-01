from django.shortcuts import render

from shows.models import Show


def index(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(
        request,
        'index.html',
        context,
    )
