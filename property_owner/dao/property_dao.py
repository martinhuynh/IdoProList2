from property_owner.models import Property
from property_owner.serializer import PropertySerializer
from user.models import User

class PropertyNotFoundError(Exception):
    pass

class PropertyDAO:
    # Lists all properties associated to user.
    def listProperties(self, user_id):
        query_set = Property.objects.filter(propertymanager_id=user_id)
        deserialized = PropertySerializer(query_set, many=True)
        return deserialized.data
    
    def getProperty(self, property_id, user_id):
        try:
            return Property.objects.get(id=property_id, propertymanager_id=user_id)
        except Property.DoesNotExist:
            # NOTE: We should not expose the user id nor property id.
            raise PropertyNotFoundError(f'Property ID {property_id} for user {user_id} not found.')
    
    # Checks if the property is owned by the user.
    def verify(self, property_id, user_id):
        return self.getProperty(property_id, user_id) is not None

    # Updates a property associated with the user.
    def updateProperty(self, property_id, user_id, new_property_data):
        # Verify the property is owned by 
        property = Property.objects.get(id=property_id, propertymanager_id=user_id)
        serializer = PropertySerializer(property, data=new_property_data)
        if serializer.is_valid():
            serializer.save()
            print('VALID')
        else:
            print('INVALID')
        return serializer.data
