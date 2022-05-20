from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.
# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username/
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Institution(models.Model):
    TYPES = (
        (1, "fundacja"),
        (2, "organizacja pozarządowa"),
        (3, "zbiórka lokalna"),
        )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    i_type = models.IntegerField(choices=TYPES, default=1) 
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
