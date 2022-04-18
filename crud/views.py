from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post 



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'crud/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'crud/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering =['-date_posted']
    paginate_by = 9


class UserPostListView(ListView):
    model = Post
    template_name = 'crud/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self) :
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image','name','age','gender','last_seen_date','last_seen_location', 'description']
            

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image','name','age','gender','last_seen_date','last_seen_location','description']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'crud/about.html',{'title': 'About'})



