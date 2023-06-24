from django.contrib.auth.models import AbstractUser, BaseManagerUser
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")

        email = extra_fields.setdefault("email", "admin.admin.com")
        self.normalize_email(extra_fields['email'])

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True")

        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True) # primary key
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_signup = models.BooleanField() # boolean
    has_consent = models.BooleanField() # boolean

    objects = UserManager()
    REQUIRED_FIELDS = ['username', 'password', 'email']

    def __str__(self):
        return self.user_id
