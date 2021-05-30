from django.db.models import query
from rest_framework.response import Response
from rest_framework import generics
from .models import Posts
from .serializers import PostsSerializer, serializers

class PostView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
       queryset = self.get_queryset()
       serializers = PostsSerializer(queryset, many=True)
       return Response(serializers.data)
    