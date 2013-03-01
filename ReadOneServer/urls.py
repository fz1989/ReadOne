from django.conf.urls import patterns, include, url
from regist.views import *
from competition.views import *
from friends.views import *
from items.views import *
from login.views import *
from rank.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReadOneServer.views.home', name='home'),
    # url(r'^ReadOneServer/', include('ReadOneServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^regist/$', regist),
    ('^competition/$', competition),
    ('^friends/$', friends),
    ('^items/$', items),
    ('^login/$', login),
    ('^rank/$', rank),

)
