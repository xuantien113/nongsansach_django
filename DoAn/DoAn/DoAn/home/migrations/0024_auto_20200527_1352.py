# Generated by Django 3.0.6 on 2020-05-27 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20200527_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcontent',
            old_name='slig',
            new_name='slug',
        ),
    ]
