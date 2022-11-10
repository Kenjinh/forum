from rest_framework import serializers
from .models import *

# Create your serializers here.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

