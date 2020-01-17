from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import Serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import  TokenAuthentication
from profiles_api import permissions


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
    
