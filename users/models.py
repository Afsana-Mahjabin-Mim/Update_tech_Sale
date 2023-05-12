from django.db import models 
from django.contrib.auth.models import (AbstractBaseUser)
from django.contrib.auth.models import BaseUserManager
import random 

class UserManager(BaseUserManager):
    def create_user(self,email,user_name,phone_number,address, password=None,**kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            phone_number=phone_number,
            address=address,
        )
       
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,user_name,phone_number,address, password=None,**kwargs):
        """
        Creates and saves a superuser with the given email,
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            user_name=user_name,
            phone_number=phone_number,
            address=address,
        )
    
        user.is_admin = True
        user.is_superuser=True 
        user.save(using=self._db)
        return user 

class User(AbstractBaseUser):
    user_name=models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    ) 
    phone_number=models.CharField(max_length=20, null=True, blank=True)
    address=models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','phone_number']
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin 

