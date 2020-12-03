from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, PostDetailView, \
     AddCategoryView, LikeView, DisLikeView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/', AddCategoryView.as_view(), name="add-category"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about"),
    path('contactus/', views.contactus, name="contactus"),
    path('post/<int:pk>/comment', views.PostCommentView.postComment, name="post-comment"),
    path('dislike/<int:pk>', DisLikeView, name='dislike_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('search/', views.search, name='search'),
]

