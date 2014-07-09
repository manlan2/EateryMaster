from django.conf.urls import patterns, include, url
from CookeryMaster import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EateryMaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^signup/', views.signup),
    url(r'^login/', views.login),
    url(r'^logout/',views.logout),
    url(r'^about/',views.about),
    url(r'^guestbook/',views.guestbook),
)