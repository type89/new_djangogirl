from django.urls import path
from . import views
#from django.conf.urls import url, include

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #url(r'^tag/(?P[-w]+)/$', views.post_list, name='post_list_by_tag'),
    #path('tag/(?P[-w]+)/', views.post_list, name='post_list_by_tag'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new', views.post_new, name='post_new'),
]
