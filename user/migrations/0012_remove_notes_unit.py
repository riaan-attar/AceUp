# Generated by Django 5.1 on 2024-08-17 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_merge_0008_docs_0010_notes_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='unit',
        ),
    ]
