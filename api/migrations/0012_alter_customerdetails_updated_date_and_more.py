# Generated by Django 4.0.4 on 2022-04-26 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_customerdetails_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 19, 25, 50, 65071, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='discountpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 19, 25, 50, 64632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rewardpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 19, 25, 50, 64164, tzinfo=utc)),
        ),
    ]
