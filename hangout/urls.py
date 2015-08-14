import os
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Example:
    url('^$', 'hangout.views.index'),
    url('^oauth2callback', 'hangout.views.auth_return'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url('^admin/', include(admin.site.urls)),
    url('^accounts/login/$', auth_views.login,
        {'template_name': 'plus/login.html'}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
]
