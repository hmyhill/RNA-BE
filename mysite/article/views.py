#Importing modules to configure the views
from django.shortcuts import render
from .models import Post
from django.views import generic
from django.shortcuts import render, redirect

#User views the articles filtered by published articles sorted by created articles
class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name= 'posts'

#Setting the view of the article once user clicks on it
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name= 'post'

class BlogSearchView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query).order_by('-created_on')