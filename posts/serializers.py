from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    user = PostUserSerializer(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'image', 'created_at', 'updated_at', 'likes_count', 'comments_count']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'likes_count', 'comments_count']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class PostDetailSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields