from django.urls import path
from blog import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('',PostListView.as_view(), name="blog-home"),
    #this neeeds  a appname/model_viewtype, for this case its, blog/post.list. You can also change the template that this class 
    #model would want
    path('about/', views.about, name="blog-about"),
    path('contact-us/', views.contact, name="contact-us"),
    #creating a dynamic route so we can see each post individually
    path('post/<int:pk>',PostDetailView.as_view(), name="post-detail"),
    #this one needs a tempalte with name post_form
    path('post/new/',PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name="post-delete"), # this needs a confirm_post_delete html template
    path('user/<str:username>',UserPostListView.as_view(), name="user-posts"),
         
]