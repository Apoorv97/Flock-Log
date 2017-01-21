"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),
	
	#Topics Page
	url(r'^topics/$', views.topics, name='topics'),
	
	# Detail page for a single topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	
	#Page for adding a new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	
	#Page for adding a new entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	
	#Page for editing an entry
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
	
	#events page
	url(r'^events/$', views.events, name='events'),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



