from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 's21133135.views.home', name='home'),
    # url(r'^s21133135/', include('s21133135.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^get_log/$', 'myapp.views.get_log', name='get_log'),
    url(r'^submit/$', 'myapp.views.submit', name='submit'),
    url(r'^results/$', 'myapp.views.results', name='results'),
)
