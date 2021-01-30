from rest_framework import serializers

from .models import Profile, Comment, Post
from social import views

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	# posts = serializers.SlugRelatedField(many=True,queryset=Post.objects.all(),slug_field='title')

	class Meta:
		model = Profile
		fields = (
	        'id',
	        'name',
	        'username',
	        'email',
	        'phone',
	        'website',
        )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	# postId = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')

	class Meta:
		model = Comment
		fields = (
			'id',
			'name',
			'email',
			'body'
		)


class PostSerializer(serializers.HyperlinkedModelSerializer):
	# comments = serializers.PrimaryKeyRelatedField(many=True,queryset=Comment.objects.all())	
	# comments = serializers.SlugRelatedField(many=True,queryset=Comment.objects.all(),slug_field='name')
	comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
	
	class Meta:
		model = Post
		fields = (
			'userId',
			'id',
			'title',
			'body',
			'comments',
		)


class UserStatisticsSerializer(serializers.ModelSerializer):
    total_posts = serializers.IntegerField(read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    class Meta:
        model = Profile
        fields = (
        	'id',
        	'name',
        	'total_posts',
        	'total_comments'
        )