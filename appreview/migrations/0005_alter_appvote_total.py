# Generated by Django 3.2.7 on 2021-09-23 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreview', '0004_alter_appvote_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appvote',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]
