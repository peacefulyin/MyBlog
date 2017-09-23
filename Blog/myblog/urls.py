#coding=utf-8
from django.conf.urls import url
from myblog import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/home')),
    url(r'^(home|lifestyle|piano|geek)', views.index, name='index'),
    url(r'^send_data$', views.send_data),
    url(r'^getArticals/(\d+)$', views.return_articals),
    url(r'^send_comment$', views.receive_comment),
    url(r'^get_comments/(\d+)$', views.return_comments),
    url(r'^about/$',views.about),
    url(r'^artical/(\d+)$',views.show_artical,name='artical'),
    url(r'^base$', views.base),

]
