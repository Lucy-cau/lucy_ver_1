# Generated by Django 4.0.4 on 2022-09-25 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='locker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.locker'),
        ),
    ]
