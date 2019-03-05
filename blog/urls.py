from django.urls import path
# from .views import (
# 	PostListView,
# 	PostDetailView,
# 	PostCreateView,
# 	PostUpdateView,
# 	PostDeleteView,
# 	UserPostListView
# )
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #homepage - function-based
    path('file/upload/', views.file_upload, name='file-upload'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    # path('', PostListView.as_view(), name='blog-home'), #homepage - class-based
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
