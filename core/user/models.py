from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your views here.

class MyUserManager(UserManager):
    def _create_user(self, phone_number, email, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone number must be set")

        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)
    
    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)
    

ROLE_CHOICES = ( 
    ("CUS", "Customer"), 
    ("ADM", "Admin"), 
    ("REP", "Repair Man"), 
) 


class MyUser(AbstractUser):

    ROLE_CHOICES = ( 
    ("CUS", "Customer"), 
    ("REP", "Repair Man"), 
    ) 

    username = None
    role = models.CharField(max_length=16,choices=ROLE_CHOICES, default='CUS')
    email = models.EmailField(unique=False, blank=True)
    phone_number = PhoneNumberField(unique=True)

    USERNAME_FIELD = "phone_number"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [role]
    objects = MyUserManager()

    def __str__(self):
        return str(self.phone_number)
