from rest_framework import serializers # type: ignore
from blogs.models import BlogPost
from comments.models import UserComments
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from likes.models import Like

# class BlogPostWithComments(serializers.ModelSerializer):
    
#     user_name = serializers.StringRelatedField(source='user_id.username', read_only=True)
    
#     class Meta:
#         model = UserComments
#         fields = ['user_name','content','date_posted']
#         read_only_fields = ['user_name','date_posted']

# class BlogPostLikeSerializer(serializers.ModelSerializer):
        
#     class Meta:
#         model = Like
#         fields = ['post','user','created_at']
#         read_only_fields = ['post','user','created_at']









class BlogListSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['author','email','date_published','url']
        read_only_fields = ['author','email','date_published','url']
    
    def get_email(self,obj):
        return User.objects.get(id=obj.author.id).email
    

# class BlogPostSerializer(serializers.ModelSerializer):
#     author = serializers.StringRelatedField(source='author.username', read_only=True)
#     comments = serializers.SerializerMethodField()
#     likes = serializers.SerializerMethodField()
#     email = serializers.SerializerMethodField()

#     class Meta:
        
#         model = BlogPost
#         fields = ['title', 'content', 'author', 'date_published', 'comments','likes','email']
#         read_only_fields = ['author','date_published','likes','email']  
    
#     def get_comments(self,obj):
#         return reverse('comment-list',kwargs = {'blog_post_id':obj.id}, request=self.context.get('request'))
    
#     def get_likes(self,obj):
#         total_likes = Like.objects.filter(post = obj.id).count()
#         return total_likes
    
#     def get_email(self,obj):
#         return User.objects.get(id=obj.author.id).email

