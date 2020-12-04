from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from users.forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from Blog.models import Post
from django.contrib import messages


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def DisLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_idd'))
    post.dislikes.add(request.user.id)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def AddReplyView(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post = post
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        reply_id = request.POST['comment_id']
        reply_qs = None
        if reply_id is not None:
            reply_qs = Comment.objects.get(id=reply_id)
        comments = Comment(user=name, post=post, comment=comment, reply=reply_qs)
        comments.save()
        return redirect('comment', pk=pk)
    else:
        return render(request, 'blog/add_comment.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    model = Post
    template_name = 'blog/post_detail.html'


class PostCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'tags', 'category', 'header_image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = Category.objects.all()
        return context

    def AddCatView(self, request, pk):
        category = get_object_or_404(Post, id=request.POST.get('submit'))
        category.choices.__add__(self, request.user.id)
        return HttpResponseRedirect(reverse('add-category', args=[str(pk)]))


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def contactus(request):
    return render(request, 'blog/contactus.html')


def search(request):
    query = request.GET['query']
    if len(query) > 80:
        posts = Post.objects.none()
    else:
        poststitle = Post.objects.filter(title__icontains=query)
        postcontent = Post.objects.filter(content__icontains=query)
        posts = poststitle.union(postcontent)
    if posts.count() == 0:
        messages.warning(request, "No search result found please refine your query")
    params = {'posts': posts, 'query': query}
    return render(request, 'blog/search.html', params)
