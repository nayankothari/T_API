# Generated by Django 4.0.4 on 2022-04-25 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 17, 57, 6, 991904, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='discountpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 17, 57, 6, 991499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rewardpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 25, 17, 57, 6, 991072, tzinfo=utc)),
        ),
    ]
