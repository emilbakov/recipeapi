# Generated by Django 2.2.1 on 2019-06-07 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190607_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='allergy',
            new_name='allergys',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='course',
            new_name='courses',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cousine',
            new_name='cousines',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='diet',
            new_name='diets',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='holiday',
            new_name='holidays',
        ),
    ]
