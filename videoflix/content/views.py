from unittest.mock import DEFAULT
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from videoflix.videoflix.settings import CACHES, CACHES_TTL
from django.core.cache.backends.base import DEFAULT_TIMEOUT


CACHES_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
@cache_page(CACHES_TTL)
@login_required(login_url='/login/')
def index(request):
    pass