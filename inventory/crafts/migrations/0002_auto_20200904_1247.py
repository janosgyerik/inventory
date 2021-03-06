# Generated by Django 3.1.1 on 2020-09-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='source_url',
        ),
        migrations.AddField(
            model_name='material',
            name='vendor_url',
            field=models.URLField(blank=True, help_text='Vendor / website URL to buy more'),
        ),
        migrations.AlterField(
            model_name='product',
            name='hours_to_make',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='target_price',
            field=models.FloatField(blank=True),
        ),
    ]
