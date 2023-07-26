from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from .models import *

# Create your views here.


class PostList(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4
    page_kwarg = 'page'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

