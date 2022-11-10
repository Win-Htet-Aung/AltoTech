from django import forms
from .models import Issue


class NewIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            "title", "description",
            "source", "file", "software_version",
        ]
