# Generated by Django 3.1.1 on 2020-09-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0003_auto_20200904_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
