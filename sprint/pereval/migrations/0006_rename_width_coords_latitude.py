# Generated by Django 4.2.7 on 2023-11-29 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0005_alter_user_options_rename_latitude_coords_width_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coords',
            old_name='width',
            new_name='latitude',
        ),
    ]