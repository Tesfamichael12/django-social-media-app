from rest_framework import serializers
from .models import Comment, Like, Follow
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        read_only_fields = ['id', 'follower', 'created_at']
    
    def validate(self, attrs):
        if attrs['following'] == self.context['request'].user:
            raise serializers.ValidationError("You cannot follow yourself.")
        return attrs
    
    def create(self, validated_data):
        validated_data['follower'] = self.context['request'].user
        return super().create(validated_data)

class FollowerSerializer(serializers.ModelSerializer):
    follower = CommentUserSerializer()
    
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'created_at']

class FollowingSerializer(serializers.ModelSerializer):
    following = CommentUserSerializer()
    
    class Meta:
        model = Follow
        fields = ['id', 'following', 'created_at']