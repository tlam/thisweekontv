from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from shows.models import Show


def index(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    context = {
        'episodes': show.episode_set.order_by('air_date'),
        'show': show,
    }
    return render(
        request,
        'shows/index.html',
        context,
    )


def configuration(request):
    if request.method == 'POST':
        show_id = 0
        for key in request.POST.keys():
            if key.startswith('show'):
                key_name, show_id = key.split('-')
                show_id = int(show_id)
                break
        if show_id:
            try:
                show = Show.objects.get(pk=show_id)
                show.refresh()
                messages.success(request, 'Show updated')
            except Show.DoesNotExist:
                messages.error(request, 'Cannot find show with id %i' % show_id)
        else:
            messages.error(request, 'Show not found')
    context = {
        'shows': Show.objects.all(),
    }
    return render(
        request,
        'shows/configuration.html',
        context,
    )
