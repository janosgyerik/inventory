# Generated by Django 3.1.1 on 2020-09-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0010_materialtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='size',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
