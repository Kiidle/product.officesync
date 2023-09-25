# Generated by Django 4.2.4 on 2023-09-17 01:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disposition', '0005_alter_vehicle_license_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='capacity',
            field=models.CharField(max_length=20, verbose_name='Lagerkapazität*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='condition',
            field=models.CharField(choices=[('passenger_car', 'Personenwagen'), ('van', 'Kleintransporter'), ('delivery_truck', 'Lastwagen'), ('dump_truck', 'Kipplaster'), ('tanker_truck', 'Tanklastwagen'), ('tow_truck', 'Abschleppwagen'), ('pump_truck', 'Betonpumpenwagen'), ('explosive_truck', 'Sprengstofflastwagen'), ('garbage_truck', 'Müllsammellastwagen')], default='unused', max_length=20, verbose_name='Zustand*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_consumption',
            field=models.CharField(max_length=20, verbose_name='Durchschnittlicher Kraftstoffverbrauch*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(choices=[('passenger_car', 'Personenwagen'), ('van', 'Kleintransporter'), ('delivery_truck', 'Lastwagen'), ('dump_truck', 'Kipplaster'), ('tanker_truck', 'Tanklastwagen'), ('tow_truck', 'Abschleppwagen'), ('pump_truck', 'Betonpumpenwagen'), ('explosive_truck', 'Sprengstofflastwagen'), ('garbage_truck', 'Müllsammellastwagen')], default='diesel', max_length=20, verbose_name='Fahrzeugtyp*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='license_plate',
            field=models.CharField(max_length=20, verbose_name='Kennzeichen*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='manufacturer',
            field=models.CharField(max_length=20, verbose_name='Hersteller*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=20, verbose_name='Fahrzeugmodell*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[('passenger_car', 'Personenwagen'), ('van', 'Kleintransporter'), ('delivery_truck', 'Lastwagen'), ('dump_truck', 'Kipplaster'), ('tanker_truck', 'Tanklastwagen'), ('tow_truck', 'Abschleppwagen'), ('pump_truck', 'Betonpumpenwagen'), ('explosive_truck', 'Sprengstofflastwagen'), ('garbage_truck', 'Müllsammellastwagen')], default='passenger_car', max_length=20, verbose_name='Fahrzeugtyp*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=20, verbose_name='Identifikationsnummer*'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year_of_manufacturer',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900)], verbose_name='Baujahr*'),
        ),
    ]