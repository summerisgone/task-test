from django.conf.urls.defaults import *
from django.contrib import admin
from tasktest.views import ReadyView, IndexView

admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('tasktest.views',
     url(r'^$', IndexView.as_view(), name='index'),
     url(r'^load/$', 'load', name='load'),
     url(r'^ready/$', ReadyView.as_view(), name='ready'),
)

urlpatterns += patterns('djcelery.views',
    url(r'^apply/(?P<task_name>.+?)/', 'apply'),
    url(r'^(?P<task_id>[\w\d\-]+)/done/?$', 'is_task_successful',
        name="celery-is_task_successful"),
    url(r'^(?P<task_id>[\w\d\-]+)/status/?$', 'task_status',
        name="celery-task_status"),
    url(r'^tasks/', 'registered_tasks', name='task_list'),
)
