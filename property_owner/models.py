from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Represents a property such as home, apartment, etc managed and/or owned by property owner.
class Property(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now_add=True)

    # User can be a property manager, property owner, etc.
    propertymanager_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

# Work orders for each property. The orders for example are for maintenance requests, repair requests, etc.
class WorkOrder(models.Model):
    # More statuses can be added later for more detailed tracking.
    class Status(models.TextChoices):
        Created = "CR", _("Created")
        InProgress = "IP", _("InProgress")
        Completed = "CM", _("Completed")

        def get(input):
            match input:
                case "CR":
                    return Created
                case "IP":
                    return InProgress
                case "CM":
                    return Completed

    property_id = models.ForeignKey('Property', on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Created)
    description = models.TextField(blank=True, null=True)

    # Should include a public order id