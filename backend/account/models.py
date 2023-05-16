from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username,realname, password=None, **extra_fields):
        if not realname:
            raise ValueError('Must have a user name')
        if not email:
            raise ValueError('Must have a user email')
        if not username:
            raise ValueError('Must have a user username')
        user = self.model(
            email=self.normalize_email(email),
            realname=realname,
            username = username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password=None, **extra_fields):
        
        ##user = self.create_user(
            ##email,
            ##password = password,
            ##name = name,
            ##username = username
            ##)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
    
        return self.create_user(email, realname, username ,password, **extra_fields)


class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    username = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    realname = models.CharField(default='', max_length=100, null=False, blank=False)
    age = models.IntegerField()
    about_me = models.CharField(default='', max_length=500, null=True, blank=True)
    major = models.CharField(default='', max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False)
    username = models.CharField(default='', max_length=100, null=False, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','username', 'realname', 'age', 'gender','major']

    def __str__(self):
        return self.username
