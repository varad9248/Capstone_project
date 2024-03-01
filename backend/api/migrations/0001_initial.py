# Generated by Django 4.1.13 on 2024-03-01 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSearch',
            fields=[
                ('search_id', models.IntegerField(primary_key=True, serialize=False)),
                ('search_prompt', models.CharField(max_length=255, null=True)),
                ('search_count', models.IntegerField(default=0)),
                ('searched_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('rating', models.FloatField(null=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('image_url', models.URLField()),
                ('source_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('domain', models.CharField(max_length=255, null=True)),
                ('search_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productsearch')),
            ],
        ),
        migrations.CreateModel(
            name='PriceTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PriceChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_type', models.CharField(max_length=10)),
                ('change_timestamp', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(max_length=10)),
                ('alert_timestamp', models.DateTimeField(auto_now_add=True)),
                ('price_change_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]