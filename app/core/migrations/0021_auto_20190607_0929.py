# Generated by Django 2.2.1 on 2019-06-07 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20190607_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='allergys',
            new_name='allergy',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='courses',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cousines',
            new_name='cousine',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='diets',
            new_name='diet',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='holidays',
            new_name='holiday',
        ),
    ]