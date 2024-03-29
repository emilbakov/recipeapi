# Generated by Django 2.2.1 on 2019-05-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190529_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritions',
            name='calcium',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='calories',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='fat_calories',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='fibers',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='iron',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='proteins',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='sat_fat',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='sodium',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='sugar',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='total_carb',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='total_fat',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='trans_fat',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='nutritions',
            name='vitamins',
            field=models.IntegerField(default=True),
        ),
    ]
