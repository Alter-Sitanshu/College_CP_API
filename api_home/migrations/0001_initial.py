# Generated by Django 5.1.3 on 2024-12-05 07:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("CF_username", models.CharField(max_length=100)),
                ("CF_rating", models.IntegerField(blank=True, default=0)),
                ("SEM_SPI_List", models.JSONField(blank=True, default=dict)),
                ("created_on", models.DateField(default=django.utils.timezone.now)),
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
