# Generated by Django 3.0.1 on 2020-01-06 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0013_commentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
