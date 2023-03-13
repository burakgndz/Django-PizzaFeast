from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator

class MyUser(AbstractUser):

    phone_number = models.PositiveSmallIntegerField(unique=True,blank=True, null=True)
    tc_no = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)
    card_no = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)
    cv2 = models.PositiveSmallIntegerField(unique=True, blank=True, null=True)
    exp_month = models.PositiveSmallIntegerField(blank=True, null=True)
    exp_year = models.PositiveSmallIntegerField(blank=True, null=True)

   