from tweet.models import Tweet, Comment
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from account.serializers import CustomUserSerializer
from account.models import CustomUser
from django.shortcuts import get_object_or_404

class TweetSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    likes = CustomUserSerializer(many=True, required=False)

    class Meta:
        model = Tweet
        fields = "__all__"

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = get_object_or_404(CustomUser, username=author_data['username'])
        tweet = Tweet.objects.create(author=author, **validated_data)
        return tweet

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        likes_data = validated_data.pop('likes')
        instance.content = validated_data.get('content', instance.content)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        for like in likes_data:
            user = CustomUser.objects.get(username=like['username'])
            instance.likes.add(user)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    likes = CustomUserSerializer(many=True, required=False)
    post_connected = TweetSerializer()
    
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        post_connected_data = validated_data.pop('post_connected')
        post_connected = get_object_or_404(Tweet, author__username=post_connected_data['author']['username'], date_posted=post_connected_data['date_posted'])
        author_data = validated_data.pop('author')
        likes_data = validated_data.pop('likes')
        author = get_object_or_404(CustomUser, username=author_data['username'])
        comment = Comment.objects.create(post_connected=post_connected, author=author, **validated_data)
        comment.save()
        comment.likes.set(likes_data)
        return comment

    def update(self, instance, validated_data):
        post_connected_data = validated_data.pop('post_connected')
        author_data = validated_data.pop('author')
        likes_data = validated_data.pop('likes')
        instance.content = validated_data.get('content', instance.content)
        instance.data_posted = validated_data.get('date_posted', instance.date_posted)
        for like in likes_data:
            user = CustomUser.objects.get(username=like['username'])
            instance.likes.add(user)
        instance.save()
        return instance
