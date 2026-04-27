from django.urls import path

from . import views
from property_owner.features.work_order import WorkOrderView, WorkOrdersView

urlpatterns = [
    path("test/", views.Test.as_view(), name="test"),
    path("properties/", views.Properties.as_view()),
    path("property/", views.Property.as_view()),
    path("property/<int:pk>/", views.Property.as_view()),
    path("work-order/", WorkOrderView.as_view()),
    path("work-order/<int:work_order_id>/", WorkOrderView.as_view()),
    path("work-orders/", WorkOrdersView.as_view())
]