#urlpatterns = [
#    url(r'^$', 'blog.views.home', name='home'),
#]

#coding: utf-8
from django.conf.urls import url
from blog.views import home, about, show_post, contact, search

#from blog.views import PostsListView, PostDetailView

urlpatterns = [
#url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
#url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером

    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', show_post, name='post'),
    url(r'^search/$', search, name='search'),
]
