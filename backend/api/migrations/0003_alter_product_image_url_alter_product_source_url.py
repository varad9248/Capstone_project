# Generated by Django 4.1.13 on 2024-03-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_productsearch_search_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='source_url',
            field=models.URLField(max_length=1000),
        ),
    ]
