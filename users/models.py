from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from PIL import Image

class UserManager(BaseUserManager):
    #the user manager handles the data stored in the user attributes for each user instance and holds methods for creating new users and superusers
    def create_user(self, name:str, last_name:str , email:str, password:str = None, is_staff=False, is_superuser=False) -> "User":
        """function checks for the required user fields, sets user attributes to their allocated values and creates a normal user"""
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        return user

    def create_superuser(self, name: str, email:str, password:str) -> "User":
        '''contains a function similar to the create_user method but missing the last_name attribute'''
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a first name")
        
        user = self.model(email=self.normalize_email(email))
        user.name = name
        #user.region = region
        #user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        '''user = self.create_user(
            name=name,
            last_name= last_name,
            email= email,
            password=password,
            is_staff=True,
            is_superuser=True
        )'''
        user.save()

'''class to specify new user fields'''
class User(AbstractUser):
    #this class is blueprint of each user instance including their attributes that will be stored in the site
    name = models.CharField(verbose_name="Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name" , max_length=255)
    password = models.CharField(max_length= 255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    username = models.CharField(verbose_name="Name", max_length=255)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
