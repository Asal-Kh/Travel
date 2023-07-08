# Generated by Django 4.2.3 on 2023-07-08 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('total_passengers', models.IntegerField()),
                ('passengers', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(default=1)),
                ('terminal', models.IntegerField(default=1)),
                ('included_Baggage', models.IntegerField(default=20)),
                ('type', models.CharField(default='economy', max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flights', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
            ],
        ),
    ]
