# Generated by Django 3.0.1 on 2020-01-01 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('Medellin', 'Medellin'), ('Bogota', 'Bogota'), ('Neiva', 'Neiva'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Santa Marta', 'Santa Marta'), ('Ibague', 'Ibague'), ('Pereira', 'Pereira'), ('Manizales', 'Manizales')], default='Bogota', max_length=50)),
                ('picture', models.CharField(max_length=120)),
                ('likes', models.IntegerField(default=0, max_length=6)),
                ('unlikes', models.IntegerField(default=0, max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_room', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=2)),
                ('room_type', models.CharField(max_length=30)),
                ('hotel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='booking.Hotel', verbose_name='Hotel')),
            ],
        ),
    ]
