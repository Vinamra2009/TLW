from django.db import models
#overwrite custom user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#import the default user manager
from django.contrib.auth.models import BaseUserManager


#Manager files for the models below

class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    #For creating the user
    def create_user(self, email, name, password = None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have a email address')
        
        email=self.normalize_email(email)
        user = self.model(email = email,name = name)
        user.set_password(password)
        #Save user model
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """Create a new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        #These roles are from Mixin

        

# Create your models here.

#Create user class from two
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Specify model manager to create user model from this
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #In this function we have self since the function is written in a class
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        #Returning string rep of the user
        return self.email
