# Generated by Django 5.1.2 on 2024-10-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_product_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Parent_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
