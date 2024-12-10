from rest_framework import serializers # type: ignore
from blogs.models import BlogPost
from comments.models import UserComments
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

class BlogPostWithComments(serializers.ModelSerializer):
    
    user_name = serializers.StringRelatedField(source='user_id.username', read_only=True)
    
    class Meta:
        model = UserComments
        fields = ['user_name','content','date_posted']
        read_only_fields = ['user_name','date_posted']



class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username', read_only=True)
    comments = serializers.SerializerMethodField()
    class Meta:
        
        model = BlogPost
        fields = ['title', 'content', 'author', 'date_published', 'comments']
        read_only_fields = ['author','date_published']  
    
    def get_comments(self,obj):
        return reverse('comment-list',kwargs = {'blog_post_id':obj.id},request=self.context.get('request'))
