from django.conf.urls import url

from . import views

app_name = 'btwn'
urlpatterns = [
    url(r'^$', views.Newest.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<post_id>[0-9]+)/comment$', views.comment_create_view, name='comment_create'),
    url(r'^comment/(?P<pk>[0-9]+)$', views.CommentDetailView.as_view(), name='comment_detail'),
    url(r'^newest$', views.Newest.as_view(), name='post_newest'),
    url(r'^post_create', views.post_create_view, name='post_create'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^register$', views.register_view, name='register'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^profile', views.login_view, name='profile'),  # todo
    url(r'^feed/(?P<pk>[0-9]+)$', views.feed, name='feed')
]
