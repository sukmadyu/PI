from django.conf.urls import patterns, include, url
from django.contrib import admin
from blsm import urls_blsm


urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'blsm.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^login/$', views.login_view,name='login'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^ahp/',include(urls_blsm)),
)

