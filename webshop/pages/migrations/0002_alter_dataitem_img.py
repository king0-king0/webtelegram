# Generated by Django 5.1.1 on 2024-09-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataitem',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/%m/%d'),
        ),
    ]
