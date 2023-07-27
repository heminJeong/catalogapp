from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.core.paginator import Paginator
from .models import *
from .forms import EmailPostForm, CommentForm

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


class PostShare(TemplateView):
    def get(self, request, pk):

        post = get_object_or_404(Post, id=pk)
        form = EmailPostForm()
        return render(request, 'post_share.html', {'post': post, 'form': form, 'sent': False})


    def post(self, request, pk):
        form = EmailPostForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, id=pk)
            data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{data['name']} 님이 {post.title}을(를) 추천합니다."
            message = f"{post.title}을 {post_url}에서 읽어보세요.\n\n" \
                      f"{data['name']}님의 읜견 : {data['comments']}"
            send_mail(subject, message, 'jhemin0415@gmail.com', [data['to']])
            return render(request, 'post_share.html', {'post': post, 'form': form, 'sent': True})
