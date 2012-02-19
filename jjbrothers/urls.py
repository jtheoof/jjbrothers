from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jjbrothers.portal.views.weddings', name='weddings'),
    # url(r'^jjbrothers/', include('jjbrothers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(
			r'^/?bootstrap/(?P<path>.*)$', 
			'django.views.static.serve', 
			{'document_root': (os.path.dirname(os.path.abspath(__file__)) + '/./static/bootstrap')}
		),
		(
			r'^/?jjb/(?P<path>.*)$', 
			'django.views.static.serve', 
			{'document_root': (os.path.dirname(os.path.abspath(__file__)) + '/./static/jjb')}
		),
	)
