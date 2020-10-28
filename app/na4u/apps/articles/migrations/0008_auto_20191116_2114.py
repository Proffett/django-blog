# Generated by Django 2.2.4 on 2019-11-16 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20191116_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comment_article', to='articles.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 16, 21, 14, 8, 881970, tzinfo=utc), verbose_name='date'),
        ),
    ]