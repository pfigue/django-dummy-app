from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^store/', include('dummy.store.urls')),
)
