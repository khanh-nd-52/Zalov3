from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly, IsOwnerOrPostOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer, PostSerializerCreate


# class PostView(APIView):
#
#     @staticmethod
#     def get(request):
#         """
#         List posts
#         """
#
#         posts = Post.objects.all()
#         # posts = post_filter(request, posts)
#         if type(posts) == Response:
#             return posts
#         return Response(PostSerializer(posts, many=True).data)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AddPostView(generics.CreateAPIView):

    # @staticmethod
    # def get(request):
    #     """
    #     List posts
    #     """
    #
    #     posts = Post.objects.all()
    #     posts = post_filter(request, posts)
    #     if type(posts) == Response:
    #         return posts
    #     return Response(PostSerializer(posts, many=True).data)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    @staticmethod
    def post(request):
        """
        Create post
        """

        serializer = PostSerializerCreate(data=request.data, context={'request': request})
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
