# Generated by Django 2.1 on 2018-09-05 17:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180905_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 5, 17, 42, 34, 749922, tzinfo=utc)),
        ),
    ]
