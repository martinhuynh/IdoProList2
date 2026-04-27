from property_owner.models import WorkOrder
from property_owner.serializer import WorkOrderOutputSerializer

class WorkOrderNotFound(Exception):
    pass

class WorkOrderDAO():
    def create(self, property_id):
        pass

    def list(self, user_id):
        work_orders = WorkOrder.objects.filter(user_id=user_id)
        return WorkOrderOutputSerializer(work_orders, many=True).data

    def updateStatus(self, status, work_order_id):
        work_order = WorkOrder.objects.get(id=work_order_id)
        serializer = WorkOrderOutputSerializer(work_order, status=status)
        serializer.save()

    def get(self, work_order_id):
        work_order = WorkOrder.objects.get(id=work_order_id)
        return WorkOrderOutputSerializer(work_order).data

    # Checks if work order is owned by user.
    def verify(self, work_order_id, user_id):
        try:
            result = WorkOrder.objects.get(id=work_order_id, user_id=user_id)
        except:
            raise WorkOrderNotFound(f"Work order {work_order_id} not found for user {user_id}.")
        return result is not None
