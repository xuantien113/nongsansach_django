# Generated by Django 3.0.6 on 2020-05-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20200527_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
