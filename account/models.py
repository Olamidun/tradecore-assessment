from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, **kwargs):
        if email is None:
            raise TypeError('Please supply a valid email')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(kwargs.get('password'))
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_verified = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    continent = models.CharField(max_length=30, null=True, blank=True)
    timezone = models.CharField(max_length=30, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    country_code = models.CharField(max_length=30, null=True, blank=True)
    name_of_holiday = models.CharField(max_length=30, null=True, blank=True)
    holiday_type = models.CharField(max_length=30, null=True, blank=True)
    weekday = models.CharField(max_length=30, null=True, blank=True)
    holiday_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = UserAccountManager()

    def __str__(self):
        return self.email

