# class PostSerializer(serializers.ModelSerializer):
#     post_reply_count = serializers.SerializerMethodField()
#     post_votes = PostVoteSerializer(many=True, read_only=True)
#     user = UserSerializer()
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#     @staticmethod
#     def get_post_reply_count(post):
#         return PostReply.objects.filter(post=post).count()
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for object author info"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'avatar')

class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post objects"""
    author = AuthorSerializer(read_only=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False)
    # number_of_comments = serializers.SerializerMethodField()
    # post_comments = serializers.SerializerMethodField(
    #     'paginated_post_comments')
    # liked_by_req_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'image',
                  'described', 'posted_on',
                  'number_of_likes',
                  'post_comments', )

        def get_number_of_comments(self, obj):
            return Comment.objects.filter(post=obj).count()

class PostSerializerCreate(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'