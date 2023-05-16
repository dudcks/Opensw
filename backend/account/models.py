from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class usermanager(BaseUserManager):
    def creat_user(slef,email,name,password=None):
        if not email:
            raise ValueError('must have user email')
        if not name:
            raise ValueError('must have user name')