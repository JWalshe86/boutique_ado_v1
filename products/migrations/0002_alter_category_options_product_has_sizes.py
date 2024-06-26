# Generated by Django 4.2 on 2024-03-31 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="product",
            name="has_sizes",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
