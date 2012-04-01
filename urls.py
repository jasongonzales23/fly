from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
from contact_us.views import contact
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fly.views.home', name='home'),
    # url(r'^fly/', include('fly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', contact),
    url(r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
    ) 