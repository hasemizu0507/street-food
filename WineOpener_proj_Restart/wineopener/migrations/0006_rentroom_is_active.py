# Generated by Django 2.2.1 on 2021-09-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wineopener', '0005_auto_20210827_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
