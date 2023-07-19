from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from api.team.models import Team
from api.subteam.models import SubTeam


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Users must have a username.")

        if 'email' in extra_fields:
            self.normalize_email(extra_fields['email'])
        # Check if username already exists
        if self.filter(username=username).exists():
            raise ValueError("Username already exists.")

        email = extra_fields.get('email')
        if email and self.filter(email=email).exists():
            raise ValueError("Email already exists.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        extra_fields.setdefault("email", f"{username}@admin.com")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True")

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)  # primary key
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_signup = models.BooleanField(default=False)  # boolean
    has_consent = models.BooleanField(default=False)  # boolean
    travel_method = models.CharField(max_length=100, blank=True, choices=[('RUNNING', 'RUNNING'), ('WHEELING', 'WHEELING'), ('WALKING', 'WALKING')])
    avatar = models.CharField(max_length=100, default="avatar1.jpg", choices=[(
        'avatar1.jpg', 'avatar 1'), ('avatar2.jpg', 'avatar 2'), ('avatar3.jpg', 'avatar 3'), ('avatar4.jpg', 'avatar 4'),
        ('avatar5.jpg', 'avatar 5'), ('avatar6.jpg', 'avatar 6')])
    subteam_id = models.ForeignKey(SubTeam, null=True, on_delete=models.SET_NULL, blank=True)
    team_id = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, blank=True)
    team_admin = models.BooleanField(default=False)
    reset_token = models.CharField(max_length=36, blank=True)
    reset_time = models.DateTimeField(null=True, blank=True)
    challenge_start_date = models.DateField(null=True, blank=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.username
