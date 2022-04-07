# Generated by Django 4.0.3 on 2022-04-05 14:05

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_alter_car_doors_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('6', '6'), ('5', '5'), ('2', '2'), ('4', '4'), ('3', '3')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Airbags', 'Airbags'), ('Grejanje sedista', 'Grejanje sedista'), ('Pomoć prilikom parkiranja', 'Pomoć prilikom parkiranja'), ('Audio interfejs', 'Audio interfejs'), ('Tempomat', 'Tempomat'), ('Direktno ubrizgavanje goriva', 'Direktno ubrizgavanje goriva'), ('Rikverc kamera', 'Rikverc kamera'), ('Servo', 'Servo'), ('Bluetooth', 'Bluetooth'), ('Klima', 'Klima'), ('Alarm', 'Alarm'), ('Auto Start/Stop', 'Auto Start/Stop')], max_length=163),
        ),
    ]
