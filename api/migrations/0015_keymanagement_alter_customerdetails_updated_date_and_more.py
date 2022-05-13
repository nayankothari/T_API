# Generated by Django 4.0.4 on 2022-05-09 18:46

import api.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_customerdetails_updated_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(default=api.models.public_key, editable=False, max_length=16, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('valid_for_days', models.CharField(choices=[('30', '30 days'), ('90', '90 days'), ('180', '180 days'), ('360', '360 days')], max_length=3)),
                ('amount', models.CharField(choices=[('0', 'Free'), ('499', '499/-'), ('1399', '1399/-'), ('2499', '2499/-'), ('3999', '3999/-')], default='Free', max_length=4)),
                ('rps', models.BooleanField(default=True)),
                ('cloud', models.BooleanField(default=True)),
                ('backup', models.BooleanField(default=True)),
                ('customer_name', models.CharField(blank=True, max_length=255)),
                ('shop_name', models.CharField(blank=True, max_length=355)),
                ('email', models.CharField(blank=True, max_length=80)),
                ('number', models.CharField(blank=True, max_length=15)),
                ('key_status', models.IntegerField(default=0)),
                ('activated_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 9, 18, 46, 41, 584229, tzinfo=utc))),
                ('system_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 18, 46, 41, 583762, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='discountpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 18, 46, 41, 583392, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rewardpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 18, 46, 41, 582905, tzinfo=utc)),
        ),
    ]