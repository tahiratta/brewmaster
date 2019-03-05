# Generated by Django 2.1.7 on 2019-02-27 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custdata', '0002_auto_20190227_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='origin_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
