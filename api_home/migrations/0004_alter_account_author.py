# Generated by Django 5.1.3 on 2024-12-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_home", "0003_alter_account_created_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="author",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
