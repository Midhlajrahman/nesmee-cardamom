# Generated by Django 5.1.4 on 2025-01-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="description",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
