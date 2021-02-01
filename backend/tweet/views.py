from django.shortcuts import render
from rest_framework import viewsets
from tweet.models import Tweet, Comment
from tweet.serializers import TweetSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    @action(detail=True, methods=['get'],)
    def comments(self, request, pk):
        queryset = Comment.objects.filter(post_connected=pk)
        serializer_class = CommentSerializer(queryset, many=True)
        return Response(serializer_class.data)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
