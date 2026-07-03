from django import forms
from .models import Meeting


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting

        fields = [
            "full_name",
            "email",
            "phone",
            "project_type",
            "preferred_date",
            "preferred_time",
            "project_description",
        ]

        widgets = {
            "preferred_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "preferred_time": forms.TimeInput(
                attrs={"type": "time"}
            ),

            "project_description": forms.Textarea(
                attrs={"rows": 4}
            ),
        }