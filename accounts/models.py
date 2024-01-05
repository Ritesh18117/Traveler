from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager



class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.TextField()
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_type =models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    description = models.TextField()
    address = models.TextField()
    images = models.ImageField(upload_to='images',default="")
    # author = models.ForeignKey()
    user = models.ForeignKey(CustomUser,models.SET_NULL,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(CustomUser,models.SET_NULL,blank=True,null=True)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user

class ReviewImages(models.Model):
    image = models.ImageField(upload_to='images/reviewImages',default="")
    place = models.ForeignKey(Review,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.place

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.name
