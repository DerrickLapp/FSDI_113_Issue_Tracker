from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "name", "reporter", "summary", "assignee", "status", "created_on"
    ]


# Register your models here.
admin.site.register(Issue, IssueAdmin)