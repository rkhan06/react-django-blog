from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import ListBlogsView, ListAuthorsView, BlogDetailView, ListCommentView, BlogCommentsView

urlpatterns = [
    path('blogs/', ListBlogsView.as_view(), name="blogs-list"),
    path('blogs/<int:id>', BlogDetailView.as_view(), name="blog-detail"),
    path('authors/', ListAuthorsView.as_view(), name="authors-list"),
    path('comments/', ListCommentView.as_view(), name="comment-list"),
    path('blogs/<int:id>/comments/',
         BlogCommentsView.as_view(), name="blog-comment-list"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
