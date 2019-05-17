from django.urls import path
from . import views
from blog.views import PostDetailView, PostListView
#from django.conf.urls import url, include

urlpatterns = [
    #path('base/', views.tag_list, name='base'),
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    #url(r'^tag/(?P[-w]+)/$', views.post_list, name='post_list_by_tag'),
    #path('tag/(?P[-w]+)/', views.post_list, name='post_list_by_tag'),
    path('about/', views.about, name='about'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new', views.post_new, name='post_new'),
    #path('tag/', views.TagSelectView.as_view(), name='tag'),
    path('tag/', views.tagform, name='tag'),
    #path('tag/<str:tag_slug>', views.tagview, name='tag'),
]
