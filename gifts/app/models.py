from django.db import models
from models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_lenght=30)


class Institution(models.Model):
    TYPES = (
        (1, "fundacja"),
        (2, "organizacja pozarządowa"),
        (3, "zbiórka lokalna"),
        )
    name = models.CharField(max_lenght=30)
    description = models.CharField(max_lenght=300)
    i_type = models.IntegerField(choices=TYPES, default=1) 
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_lenght=30)
    phone_number = models.CharField(max_lenght=30)
    city = models.CharField(max_lenght=30)
    zip_code = models.CharField(max_lenght=6)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
