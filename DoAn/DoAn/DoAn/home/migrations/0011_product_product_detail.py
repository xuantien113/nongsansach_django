# Generated by Django 3.0.6 on 2020-05-26 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_product_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Product_detail'),
        ),
    ]
