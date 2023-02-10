# Generated by Django 3.2.17 on 2023-02-09 15:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("public_website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="APICall",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("url", models.CharField(max_length=150)),
                ("PEid", models.CharField(max_length=150)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="calls",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
