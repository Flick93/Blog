from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "author", "status"]

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "author", "status"]
class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    succes_url = reverse_lazy("list")
