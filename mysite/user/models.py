from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import ExpressionWrapper, F
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay, Now


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


    def __str__(self):
        return self.username

class Profile(AbstractBaseUser):
    username = models.CharField(max_length=200, null=False, blank=False,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    #phone = models.CharField(max_length=10)
    phone = PhoneNumberField(null=True, blank=True)

    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    dob = models.DateField(null=True, blank=True)
    #state = models.CharField(max_length=40, null=True, blank=True)
    #district = models.CharField(max_length=40, null=True, blank=True)

    USERNAME_FIELD = 'username' 

    objects = MyAccountManager()
    @property
    def get_dob(self):
        return self.dob
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return "{}:{}:{}".format(self.id, self.email, self.username)

    def __str__(self):
        return f'{self.username}'
    
    
