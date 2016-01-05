from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'btwn'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<post_id>[0-9]+)/comment$', views.CommentCreate.as_view(), name='comment_create'),
    url(r'^comment/(?P<pk>[0-9]+)$', views.CommentDetailView.as_view(), name='comment_detail'),
    url(r'^newest$', views.Newest.as_view(), name='post_newest'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^register$', views.register_view, name='register'),
    url(r'^login$', auth_views.login, {
        'template_name': 'btwn/login.html'
    }, name='login'),

]
