from django.conf.urls import patterns, include, url

from django.contrib import admin

import fatecore.views as fateviews

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'$^', fateviews.index, name = 'index'),
    url(r'^new$', fateviews.new, name = 'new'),
    url(r'^characters/(?P<pk>\d+)$', fateviews.CharacterDetailView.as_view(), name = 'view'),
)
