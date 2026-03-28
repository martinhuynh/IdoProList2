from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.Test.as_view(), name="test"),
    path("properties/", views.Properties.as_view()),
    path("property/", views.Property.as_view()),
    path("property/<int:pk>/", views.Property.as_view()),
]