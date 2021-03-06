# Generated by Django 4.0.4 on 2022-04-25 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=300, unique=True)),
                ('office', models.CharField(max_length=256)),
                ('branch', models.CharField(max_length=256)),
                ('office_branch', models.CharField(blank=True, max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=datetime.datetime(2022, 4, 25, 17, 57, 1, 284218, tzinfo=utc))),
                ('customer_name', models.CharField(blank=True, max_length=256)),
                ('number', models.BigIntegerField()),
                ('alt_number', models.CharField(blank=True, max_length=256)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('card_number', models.CharField(max_length=256)),
                ('date_for_BA', models.CharField(blank=True, max_length=15)),
                ('birt_anny', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountPointSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=256)),
                ('branch', models.CharField(max_length=256)),
                ('office_branch', models.CharField(blank=True, max_length=256)),
                ('bill_number', models.CharField(blank=True, max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=datetime.datetime(2022, 4, 25, 17, 57, 1, 283831, tzinfo=utc))),
                ('mobile_number', models.BigIntegerField(blank=True)),
                ('customer', models.CharField(blank=True, max_length=256)),
                ('card_number', models.CharField(blank=True, max_length=256)),
                ('bill_amount', models.FloatField(blank=True)),
                ('points', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RewardPointSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=256)),
                ('branch', models.CharField(max_length=256)),
                ('office_branch', models.CharField(blank=True, max_length=256)),
                ('bill_number', models.CharField(blank=True, max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=datetime.datetime(2022, 4, 25, 17, 57, 1, 283342, tzinfo=utc))),
                ('mobile_number', models.BigIntegerField(blank=True)),
                ('customer', models.CharField(blank=True, max_length=256)),
                ('card_number', models.CharField(blank=True, max_length=256)),
                ('bill_amount', models.FloatField(blank=True)),
                ('points', models.FloatField(blank=True)),
            ],
        ),
    ]
