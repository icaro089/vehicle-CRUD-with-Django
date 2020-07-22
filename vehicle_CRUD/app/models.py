from django.db import models

# Create your models here.

class Owner(models.Model):
    SEX_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    name = models.CharField(max_length=25, null=False)
    birth_date = models.DateField(null=False, verbose_name='Date of Birth')
    social_security = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    profession = models.CharField(max_length=15)
    telephone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    COLOR_CHOICES = (
        ('Black', 'black'),
        ('Blue', 'blue'),
        ('Green', 'green'),
        ('Yellow', 'yellow'),
        ('White', 'white'),
        ('Red', 'red'),
        ('Gray', 'gray'),
    )
    TYPE_CHOICES = (
        ('Motorcycle', 'motorcycle'),
        ('Car', 'car'),
        ('Truck', 'truck'),
    )
    model = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=15, null=False)
    license_plate = models.CharField(max_length=8, null=False)
    color = models.CharField(max_length=10, null=False, choices=COLOR_CHOICES)
    year = models.IntegerField(max_length=4, null=False)
    price = models.FloatField(null=False)
    type = models.CharField(max_length=15, null=False, choices=TYPE_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.model