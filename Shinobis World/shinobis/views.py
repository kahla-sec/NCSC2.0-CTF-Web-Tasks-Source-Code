from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Shinobi
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)

def shinobisHome(request):
        shinobis = Shinobi.objects.all()
        return render(request, "shinobis.html", {'shinobis': shinobis})


