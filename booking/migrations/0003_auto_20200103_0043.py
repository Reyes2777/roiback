# Generated by Django 3.0.1 on 2020-01-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20200101_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=2),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('individual_room', 'Habitación Individual'), ('double_room', 'Habitación Doble'), ('double_room_2_beds', 'Habitación Doble - 2 Camas'), ('Suite', 'Suite')], max_length=30),
        ),
    ]