# Generated by Django 3.2.7 on 2021-09-20 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0004_rename_username_profile_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firstname',
            new_name='username',
        ),
    ]