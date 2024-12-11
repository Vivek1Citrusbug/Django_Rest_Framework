from rest_framework import serializers # type: ignore
from blogs.models import BlogPost
from comments.models import UserComments
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from likes.models import Like

class BlogPostWithComments(serializers.ModelSerializer):
    
    user_name = serializers.StringRelatedField(source='user_id.username', read_only=True)
    
    class Meta:
        model = UserComments
        fields = ['user_name','content','date_posted']
        read_only_fields = ['user_name','date_posted']

class BlogPostLikeSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Like
        fields = ['post','user','created_at']
        read_only_fields = ['post','user','created_at']

class BlogPostDetailSerializer(serializers.ModelSerializer):
    comments = BlogPostWithComments(many = True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['title','content','author.username','comments','likes']
        read_only_fields = ['comments','likes']

    def get_likes(self,obj):
        total_likes = Like.objects.filter(post = obj.id).count()
        return total_likes
    
class BlogPostListSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['title','content','created_by']
        read_only_fields = ['created_by']  
    
    def get_created_by(self,obj):
        post = BlogPost.objects.get(id = obj.id)
        return f"{post.author} : {post.author.email} On {post.date_published.strftime('%Y-%m-%d %H:%M:%S')}"
    

