from django.urls import path
from .views import (PostListView, PostDetailView, FilterByLeague, FilterByTeam, CreatePost, 
CommentView, DeleteComment, DeletePost)


urlpatterns = [ 
    path('', PostListView.as_view(), name='home-page'),
    path('show/<int:pk>', PostDetailView.as_view(), name='show-detail'),
    path('create/comment/<int:pk>', CommentView.as_view(), name='comment'),
    path('filter/by/league/<int:pk>', FilterByLeague.as_view(), name='filter-by-league'),
    path('filter/by/team/<int:pk>', FilterByTeam.as_view(), name='filter-by-team'),
    path('create/post', CreatePost.as_view(), name='create-post'),
    path('user/delete/comment/<int:pk>', DeleteComment.as_view(), name='delete-comment'),
    path('user/delete/post/<int:pk>', DeletePost.as_view(), name='delete-post')
]