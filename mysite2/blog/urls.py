from django.urls import path
from .views import PostList, PostDetail, PostShare

app_name='blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('tag/<tag_slug>', PostList.as_view(), name='post_list_by_tag'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/share/', PostShare.as_view(), name='post_share'),
]