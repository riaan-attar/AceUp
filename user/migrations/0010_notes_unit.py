# Generated by Django 5.1 on 2024-08-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_remove_event_description_alter_events_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="unit",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]