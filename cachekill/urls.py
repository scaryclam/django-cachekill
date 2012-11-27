from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from cachekill.testapp.views import admin_cachekill, user_view

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/foo/', admin_cachekill),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', user_view),
)
