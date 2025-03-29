from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Priority(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Issue(models.Model):
    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=128)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="assignee",
        blank=True, null=True
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail",args=[self.id])
