# Generated by Django 3.1.1 on 2020-09-05 05:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0009_material_memo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crafts.material')),
            ],
        ),
    ]