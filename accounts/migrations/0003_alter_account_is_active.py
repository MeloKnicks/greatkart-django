# Generated by Django 4.1.5 on 2023-01-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_account_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
