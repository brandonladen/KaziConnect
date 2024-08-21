from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, userName, firstName, lastName, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, userName=userName, firstName=firstName, lastName=lastName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    userName = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="profile_pictures", height_field=None, width_field=None, max_length=None, blank=True, null=True)
    
    identificationNumber = models.CharField(max_length=20, unique=True)
    phoneNumber = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    lastLogin = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    
    failed_login_attempts = models.IntegerField(default=0)
    account_locked_until = models.DateTimeField(blank=True, null=True)
    is_banned = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName', 'firstName', 'lastName']

    def __str__(self):
        return self.email

    @property
    def is_normal_user(self):
        return self.is_staff and not self.is_admin and not self.is_service_provider

    @property
    def is_admin_user(self):
        return self.is_admin

    @property
    def is_service_provider_user(self):
        return self.is_service_provider