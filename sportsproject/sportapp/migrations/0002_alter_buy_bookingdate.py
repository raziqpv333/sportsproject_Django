# Generated by Django 5.1 on 2024-10-24 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='bookingdate',
            field=models.DateField(auto_now=True),
        ),
    ]