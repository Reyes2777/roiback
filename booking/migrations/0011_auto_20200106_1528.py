# Generated by Django 3.0.1 on 2020-01-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20200105_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='price_total',
            field=models.IntegerField(null=True),
        ),
    ]
