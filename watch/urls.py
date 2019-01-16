from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home_page,name = 'home_page'),
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^upload/$', views.upload_business, name='upload_business'),
    url(r'^hood/$', views.add_hood, name='add_hood'),
    url(r'^join(?P<neighborhood_id>\d+)',views.join, name='join'),
    url(r'^leave/(?P<neighborhood_id>\d+)',views.leave, name='leave'),
    url(r'^one_hood(?P<neighborhood_id>\d+)',views.hood, name='hood'),
    url(r'^comment/(?P<post_id>\d+)', views.one_post, name='comment'),
    url(r'^post/$', views.add_post,name='add_post'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
