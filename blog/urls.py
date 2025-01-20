from django.conf.urls import url
from . import views

app_name = 'blog'  # Add explicit app namespace

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

# After uncommenting below lines, the view and endpoint show but the app
# won't work.
# from django.urls import path
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
# ]