# Generated by Django 2.2.4 on 2019-11-18 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20191116_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 13, 8, 9, 769295, tzinfo=utc), verbose_name='date'),
        ),
    ]
