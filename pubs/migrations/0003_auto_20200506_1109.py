# Generated by Django 3.0.6 on 2020-05-06 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pubs', '0002_auto_20200505_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pub',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='pub',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pub',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pub',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AddField(
            model_name='pub',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
