# Generated by Django 3.1.1 on 2020-09-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0013_auto_20200924_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='sku',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
