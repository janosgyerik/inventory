# Generated by Django 3.1.1 on 2020-09-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0008_auto_20200904_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='memo',
            field=models.TextField(blank=True),
        ),
    ]
