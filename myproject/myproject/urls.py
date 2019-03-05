
from django.contrib import admin
# from django.urls import path  # This line was there by default
from django.conf.urls import url

from boards import views

urlpatterns = [
	url(r'^$',views.home,name = 'home'),
	url(r'^boards/(?P<pk>\d+)/$',views.board_topics, name = 'board_topics'),
	url(r'boards/(?P<pk>\d+)/new/$',views.new_topic,name='new_topic'),
    url('admin/', admin.site.urls),
]
