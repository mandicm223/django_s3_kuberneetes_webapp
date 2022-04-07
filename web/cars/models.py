from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
# Create your models here.

class Car(models.Model):
    state_choice = {
        ('SO', 'Sombor'),
    }

    year_choices = []
    for r in range(2000 , (datetime.now().year + 1)):
        year_choices.append((r , r))

    features_choices = {
        ('Tempomat', 'Tempomat'),
        ('Audio interfejs', 'Audio interfejs'),
        ('Airbags', 'Airbags'),
        ('Klima', 'Klima'),
        ('Grejanje sedista', 'Grejanje sedista'),
        ('Alarm', 'Alarm'),
        ('Pomoć prilikom parkiranja', 'Pomoć prilikom parkiranja'),
        ('Servo', 'Servo'),
        ('Rikverc kamera', 'Rikverc kamera'),
        ('Direktno ubrizgavanje goriva', 'Direktno ubrizgavanje goriva'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Bluetooth', 'Bluetooth'),
    }

    door_choices = {
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),     
    }

    car_title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice ,  max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year') , choices=year_choices)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True , blank=True)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices ,max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField()
    created_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.car_title