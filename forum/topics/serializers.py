from rest_framework import serializers
from .models import *

# Create your serializers here.

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='first_name', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    user = serializers.IntegerField(source='user.id', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True, required=False)
    last_name = serializers.CharField(source='user.last_name', read_only=True, required=False)
    image = serializers.ImageField(use_url=True, required=False)
    publish_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", required=False)
    category_name = serializers.CharField(source='category.category', read_only=True)
    comments_array = serializers.SerializerMethodField('get_comments_post', read_only=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user', 'first_name', 'last_name', 'comments_array', 'image', 'publish_date', 'category', 'category_name')

    def get_comments_post(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

