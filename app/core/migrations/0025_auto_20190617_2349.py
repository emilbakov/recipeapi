# Generated by Django 2.2.1 on 2019-06-17 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20190617_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cousine',
            new_name='recipeCuisine',
        ),
    ]