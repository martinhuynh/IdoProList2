from rest_framework import generics, status
from rest_framework.response import Response
from property_owner.serializer import WorkOrderInputSerializer, WorkOrderOutputSerializer
from property_owner.dao.property_dao import PropertyDAO
from property_owner.models import WorkOrder
from dataclasses import dataclass, asdict
from property_owner.dao.work_order_dao import WorkOrderDAO

@dataclass
class WorkOrderData:
    description: str
    property_id: int
    status: WorkOrder.Status
    user_id: int

class WorkOrderView(generics.GenericAPIView):
    serializer_class = WorkOrderInputSerializer
    
    def post(self, request):
        # validate property_id exists.
        user_id = request.user.id
        property_id = request.data['property_id']

        try:
            valid = PropertyDAO().verify(property_id, user_id)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if property_id:
            description = request.data['description']
            serializer = WorkOrderOutputSerializer(data=asdict(WorkOrderData(description, property_id, WorkOrder.Status.Created, user_id)))
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Success!"}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
        # Error
        return Response({"message": "Failed!"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, work_order_id=None):
        if work_order_id:
            user_id = request.user.id

            # Verify work order is owned by user.
            try:
                WorkOrderDAO().verify(work_order_id, user_id) is False
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            result = WorkOrderDAO().get(work_order_id)
            return Response({"work_order": result}, status=status.HTTP_200_OK)
        return Response({"message": "Failed!"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, work_order_id=None):
        status = WorkOrder.Status.get(request.data['status'])
        WorkOrderDAO().updateStatus(status)

class WorkOrderDetailsView(generics.GenericAPIView):
    pass

class WorkOrdersView(generics.GenericAPIView):
    
    def get(self, request):
        user_id = request.user.id
        return Response({"work_orders": WorkOrderDAO().list(user_id)})