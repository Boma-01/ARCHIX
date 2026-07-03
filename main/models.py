from django.db import models


class Meeting(models.Model):

    PROJECT_TYPES = [
        ("Residential", "Residential"),
        ("Commercial", "Commercial"),
        ("Interior Design", "Interior Design"),
        ("Renovation", "Renovation"),
    ]

    STATUS = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20, blank=True)

    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPES
    )

    preferred_date = models.DateField()

    preferred_time = models.TimeField()

    project_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date}"