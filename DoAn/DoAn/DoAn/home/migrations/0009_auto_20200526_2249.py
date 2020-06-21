# Generated by Django 3.0.6 on 2020-05-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_product_chitiet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='chitiet',
            new_name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='quantities',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]