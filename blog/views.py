from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    #change the default template lookup to this blog/home.html instead of blog/post_list
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    #order the posts from newest to oldest
    ordering = ['-date_posted']
    paginate_by = 10
    
    
class UserPostListView(ListView):
    model = Post
    #change the default template lookup 
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    #order the posts from newest to oldest
    paginate_by = 10
    
    def get_queryset(self):
        # IF USER DOESNT EXIST return 404 page, if it does, get the user username from the URL
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
        
    
class PostDetailView(DetailView):
    model = Post
    #needs tempalte with name blog/post_detail
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    
    #override the form_valid function from the parent class, to make it so the author for the form is the user that sent the request.
    #then return using the super() function.
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    
    #this line is neccessarry to make sure that the author is still the same author when an update is made
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #This method tests that the user making the request is the same as the author of the post. 
    #Need to have UserPassesTestMixin as parameter
    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    title = {'title': "About"}
    return render(request, 'blog/about.html',title)

def contact(request):
    title = {'title': "Contact Us"}
    return render(request, 'blog/contact_us.html',title)
 

