from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from hljs_org import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^download/$', views.download, name='download'),

    url(r'^admin/', include(admin.site.urls)),

)
