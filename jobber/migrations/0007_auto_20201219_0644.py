# Generated by Django 3.1.4 on 2020-12-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobber', '0006_auto_20201212_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
