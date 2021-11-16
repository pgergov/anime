from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import cache_page

import apps.movies.views

SEARCH_VIEW_CACHE_SECONDS = 300  # 5 minutes

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        '',
        cache_page(SEARCH_VIEW_CACHE_SECONDS)(apps.movies.views.SearchView.as_view()),
        name='movies-search',
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
