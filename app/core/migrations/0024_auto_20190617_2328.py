# Generated by Django 2.2.1 on 2019-06-17 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190617_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='recipeIngredient',
        ),
    ]
