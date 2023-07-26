from django.shortcuts import render
from django.views.generic import DetailView, ListView
from models import *

# Create your views here.


class PostList(ListView):
    queryset = Post.title.all()
    context_object_name = 'posts'
    template_name = 'templates/post_list.html'



class PostDetail(DetailView):
    pass


def post_list(request):
    pass

def post_detail(request):
    pass