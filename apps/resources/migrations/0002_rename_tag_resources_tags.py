# Generated by Django 4.2.4 on 2023-09-06 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resources",
            old_name="tag",
            new_name="tags",
        ),
    ]
