# Generated by Django 5.1 on 2024-08-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_testimonial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="image",
            field=models.ImageField(upload_to="satic/photos"),
        ),
    ]
