from django.urls import path
from views import PostList, PostDetail

app_name='blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:post_id>', PostDetail.as_view(), name='post_detail')
]