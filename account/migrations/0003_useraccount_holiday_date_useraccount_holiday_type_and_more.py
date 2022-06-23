# Generated by Django 4.0.5 on 2022-06-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_useraccount_city_useraccount_continent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='holiday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='holiday_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='name_of_holiday',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='weekday',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]