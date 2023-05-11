from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class Property(models.Model):

    PROPERTY_TYPE_CHOICES = [
        ('APT', 'Apartamento'),
        ('HOUSE', 'Casa'),
        ('T-HOUSE', 'Townhouse'),
    ]

    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    land_square_meters = models.PositiveIntegerField()
    construction_square_meters = models.PositiveIntegerField()
    floors = models.PositiveIntegerField()
    address = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    parking_stalls = models.PositiveIntegerField()
    description = models.TextField()
    power_plant = models.BooleanField()
    waterhole = models.BooleanField()
    property_type = models.CharField(
        max_length=7,
        choices=PROPERTY_TYPE_CHOICES,
    )
    for_rent = models.BooleanField()
    for_sell = models.BooleanField()
    rent_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    sell_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.address} {self.description}' 
