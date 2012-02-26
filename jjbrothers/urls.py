from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.portal.views.home', name='home'),
    url(r'^weddings$', 'apps.portal.views.weddings', name='weddings'),
    url(r'^landscapes$', 'apps.portal.views.landscapes', name='landscapes'),
    url(r'^portfolios$', 'apps.portal.views.portfolios', name='portfolios'),
    url(r'^about$', 'apps.portal.views.contact', name='contact'),
    (r'^EveBruno$', redirect_to, {'url': 'https://picasaweb.google.com/100199303636029289529/EveBruno?authuser=0&authkey=Gv1sRgCJq3xZup4Lqbaw&feat=directlink'}),
    # url(r'^jjbrothers/', include('jjbrothers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == True:
	urlpatterns += patterns('',
		(
			r'^/?media/(?P<path>.*)$',
			'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
		),
	)
