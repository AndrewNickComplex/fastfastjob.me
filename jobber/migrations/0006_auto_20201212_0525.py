# Generated by Django 3.1.4 on 2020-12-12 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobber', '0005_auto_20201210_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('gardening', 'gardening'), ('delivery', 'delivery'), ('disinfect', 'disinfect'), ('virtual assistant', 'virtual assistant')], max_length=30),
        ),
    ]