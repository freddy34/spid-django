from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
import djangosaml2_spid.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((djangosaml2_spid.urls, 'djangosaml2_spid',))),
    path('', RedirectView.as_view(url=settings.SPID_BASE_URL), name='example-index')
]
