# Generated by Django 4.0.10 on 2023-07-02 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rentfurlax', '0002_remove_lineitem_furnitureoptionid_furniture_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='deliverydate',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='deliverydate',
            field=models.DateField(default=datetime.datetime(2023, 7, 2, 17, 59, 3, 807959, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='furniture',
            name='noofdays',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
