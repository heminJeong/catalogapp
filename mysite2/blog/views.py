from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.core.paginator import Paginator
from .models import *
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag

# Create your views here.


class PostList(ListView):
    def get(self, request, tag_slug=None):
        post = Post.objects.all()
        page_number = request.GET.get('page', 1)
        tag = None
        page_list_query = Post.objects.filter(status=Post.Status.PUBLISHED)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            page_list_query = page_list_query.filter(tags__in=[tag])

        paginator = Paginator(page_list_query, per_page=4)
        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)


        return render(request, 'post_list.html', {'posts':post})

    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'post_list.html'
    paginate_by = 4

class PostDetail(DetailView):

    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)

        return render(request, 'post_detail.html', {'post':post, 'form':CommentForm()})

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)

    # form =


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

