# Generated by Django 5.1.7 on 2025-03-28 01:55

from django.db import migrations


def populate_status(apps, schemaeditor):
    entries = {
        "to-do": "An issue for which work has not yet begun",
        "in-progress": "An issue currently being worked on",
        "done": "An issue for which work has been completed"
    }
    Status = apps.get_model("issues", "Status")
    for key, value in entries.items():
        role_obj = Status(name=key, description=value)
        role_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]
