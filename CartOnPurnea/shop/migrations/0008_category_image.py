# Generated by Django 5.1.2 on 2024-10-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_sku_product_variant_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=2, upload_to='category'),
            preserve_default=False,
        ),
    ]
