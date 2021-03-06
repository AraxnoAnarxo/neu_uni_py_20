# Generated by Django 3.0.4 on 2020-04-19 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200419_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 11, 36, 33, 989608)),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
