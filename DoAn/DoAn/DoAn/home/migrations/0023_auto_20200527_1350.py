# Generated by Django 3.0.6 on 2020-05-27 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_blogcontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcontent',
            old_name='slug',
            new_name='slig',
        ),
    ]
