# Generated by Django 3.0.6 on 2020-05-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_detail',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
