# Generated by Django 5.1 on 2024-08-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_event_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="description",
        ),
        migrations.AlterField(
            model_name="events",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
