from rest_framework import generics
from .models import Blog, Comment, Author
from .serializers import BlogSerializer, AuthorSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ListBlogsView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all blogs.
        """
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        blog = request.data.get('blog')
        serializer = BlogSerializer(data=blog)
        if serializer.is_valid(raise_exception=True):
            blog_saved = serializer.save()
        return Response({"success": f"Article '{ blog_saved.title }' created successfully"})


class BlogDetailView(APIView):
    def get(self, request, id):
        """
        Return a blog with specified id.
        """
        blog = get_object_or_404(Blog, pk=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)


class ListAuthorsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListCommentView(APIView):
    def post(self, request, format=None):
        comment = request.data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "Comment added"})

    def get(self, request):
        """
        Return a blog with specified id.
        """
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class BlogCommentsView(APIView):
    def post(self, request, id, format=None):
        comment = request.data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "Comment added"})

    def get(self, request, id):
        """
        Return a list of comment for a blog.
        """
        comments = Comment.objects.all().filter(blog=id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
