# Generated by Django 3.0.6 on 2020-05-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200506_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200), max_length=250, unique_for_date='publish'),
        ),
    ]
