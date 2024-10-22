# Generated by Django 5.1 on 2024-10-22 03:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0004_cartitems'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingdate', models.DateField(auto_created=True)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('pincode', models.IntegerField()),
                ('phno', models.IntegerField()),
                ('state', models.TextField()),
                ('landmark', models.TextField()),
                ('cartitems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportapp.cartitems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]