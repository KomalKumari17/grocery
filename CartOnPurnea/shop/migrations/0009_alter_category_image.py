# Generated by Django 5.1.2 on 2024-10-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category/default.jpg', upload_to='category/'),
        ),
    ]
