# Generated by Django 2.2.1 on 2019-05-29 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190528_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
