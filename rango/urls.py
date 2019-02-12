from django.conf.urls import url
from rango import views
urlpatterns = [
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
	url(r'^$', views.index, name='index'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^add_category/$', views.add_category, name='add_category'),
		views.show_category, name='show_category'),
]