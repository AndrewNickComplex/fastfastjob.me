# Generated by Django 3.1.4 on 2020-12-09 08:59

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='job',
            name='estimate_pay',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
