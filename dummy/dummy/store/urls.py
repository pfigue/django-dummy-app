from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from dummy.beers import views as beers_v

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dummy.views.home', name='home'),
    # url(r'^dummy/', include('dummy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'beers/$', 'dummy.beers.views.get_beers'),
)
