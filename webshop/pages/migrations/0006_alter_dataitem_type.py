# Generated by Django 5.1.1 on 2024-09-12 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_dataitem_place_map_dataitem_place_map_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataitem',
            name='type',
            field=models.CharField(max_length=5),
        ),
    ]
