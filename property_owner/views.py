
from rest_framework.decorators import APIView, api_view, authentication_classes
from rest_framework import generics, status
from rest_framework.response import Response, Serializer
from django.http import JsonResponse, QueryDict

from property_owner.dao.property_dao import PropertyDAO, PropertyNotFoundError
from property_owner.serializer import PropertySerializer
from rest_framework import authentication, permissions

from user.dao.user_dao import UserDAO

class Test(generics.GenericAPIView):
    def get(self, request):
        return JsonResponse({"message": "Test endpoint is working!"}, status=status.HTTP_200_OK)
    
class Properties(generics.GenericAPIView):
    def get(self, request):
        list_properties = PropertyDAO.listProperties(self, user_id=request.user.id)
        return JsonResponse({"properties": list_properties}, status=status.HTTP_200_OK)

class Property(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PropertySerializer
    
    def get_serializer_class(self):
        match self.request.method:
            case _:
                return PropertySerializer

    # Create a new property associated with the user.
    def post(self, request, pk=None):
        # TODO: check if user is making property for themselves.
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(propertymanager_id=UserDAO().getUser(user_id=request.user.id))
            return Response({"message": "Property created successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Get a property using the primary key provided.
    def get(self, request, pk=None):
        # TODO: check if user is authorized to view.
        if pk:
            try:
                property = PropertyDAO.getProperty(self, property_id=pk, user_id=request.user.id)
            except PropertyNotFoundError as e:
                return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = PropertySerializer(property)
            return Response({"property": serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Property ID must be provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Updates existing property.
    def put(self, request, pk=None):
        # TODO: check if user is authorized to update.
        if pk:
            data = PropertyDAO.updateProperty(self, property_id=pk, user_id=request.user.id, new_property_data=request.data)
            return Response({'property': data}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        # TODO: check if user is authorized to delete.
        if pk:
            try:
                property = PropertyDAO.getProperty(self, property_id=pk, user_id=request.user.id)
                property.delete()
                return Response({'message': 'Property deleted successfully!'}, status=status.HTTP_200_OK)
            except PropertyNotFoundError as e:
                return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Property ID must be provided.'}, status=status.HTTP_400_BAD_REQUEST)