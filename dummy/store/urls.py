from django.conf.urls import patterns, include, url
from store.views import StoreItemsListView

urlpatterns = patterns('',

    url(r'^/$', StoreItemsListView.as_view(), name='list-items'),
)
