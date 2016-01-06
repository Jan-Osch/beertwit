from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Newest.as_view(), name='home'),
    url(r'^private$', views.HomeFeedView.as_view(), name='private_feed'),
    url(r'^profile/(?P<pk>[0-9]+)$', views.feed, name='feed'),
    url(r'^newest$', views.Newest.as_view(), name='post_newest'),

    url(r'^post/create', views.post_create_view, name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<post_id>[0-9]+)/edit$', views.post_edit_view, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^post/(?P<post_id>[0-9]+)/comment$', views.comment_create_view, name='comment_create'),

    url(r'^comment/(?P<pk>[0-9]+)$', views.CommentDetailView.as_view(), name='comment_detail'),
    url(r'^comment/(?P<pk>[0-9]+)/edit$', views.comment_edit_view, name='comment_edit'),
    url(r'^comment/(?P<pk>[0-9]+)/delete$', views.CommentDeleteView.as_view(), name='comment_delete'),

    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^register$', views.register_view, name='register'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^account', views.login_view, name='account_settings'), # TODO add a proper view for editing the profile settings
    url(r'^follow/(?P<pk>[0-9]+)$', views.follow, name='follow'),
    url(r'^unfollow/(?P<pk>[0-9]+)$', views.unfollow, name='unfollow')
]
app_name = 'btwn'
