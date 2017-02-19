from django.conf.urls import include, url
from django.views.static import serve
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('polls.urls')),
    url(r'^polls/', include('polls.urls')),
]
if not settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$', serve,
                        {'document_root': settings.STATIC_ROOT}), ]
