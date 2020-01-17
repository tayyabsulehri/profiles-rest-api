from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import Serializers
from rest_framework import viewsets
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = Serializers.HelloSerializer

    def get(self,request,format = None):
        """return a list of api view features"""
        an_apiview = ['used http method as function(get,post,put,path,delete) 1111']
        return Response({'message':'hello','an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Method': 'Put'})


    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'Method': 'Patch'})

    def delete(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'Method': 'Delete'})


class HelloViewSets(viewsets.ViewSet):
    """Test API view set"""
    serializer_class = Serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewsets=[
            'Uses actions (list,create,view,update)',
            'Autiomatically maps a']
        return Response({'message': 'hello', 'an_apiview': a_viewsets})

    def create(self, request):
        """Handles a partial update of an object"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk = None):
        return Response({'Method': 'Get'})

    def update(self,request,pk = None):
        return Response({'Method': 'update'})

    def partial_update(self,request,pk = None):
        return Response({'Method': 'patch'})

    def destroy(self, request, pk = None):
        return Response({'Method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """user profile viewset"""
    serializer_class=Serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle create suer authentication token"""
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = Serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)