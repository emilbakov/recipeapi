# Generated by Django 2.2.1 on 2019-06-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20190607_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='core.Ingredient'),
        ),
    ]