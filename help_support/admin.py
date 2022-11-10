from django.contrib import admin
from .models import Issue, Department


class IssueAdmin(admin.ModelAdmin):
    fields = ["title", "status", "source", "software_version", "department"]
    list_display = ["title", "status", "source", "software_version", "get_departments"]
    list_filter = ["department", "status", "source", "software_version"]
    
    def get_departments(self, obj):
        return " | ".join([p.name for p in obj.department.all()])


admin.site.register(Department)
admin.site.register(Issue, IssueAdmin)
