# Generated by Django 5.1.4 on 2025-01-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0004_remove_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Logo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=180)),
                ("image", models.ImageField(upload_to="logs/")),
            ],
            options={
                "verbose_name": "Logo",
                "verbose_name_plural": "Logos",
            },
        ),
    ]