from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permissions_classes = (permissions.IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = (permissions.IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    