from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class SystemUser(AbstractBaseUser):
    USER_CHOICES = (
        ('admin', 'admin'),
        ('translator', 'translator'),
        ('quality_assurance', 'quality_assurance'),
    )

    type = models.CharField(
        choices=USER_CHOICES,
        default='translator',
        max_length=25,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    name = models.CharField(
        max_length=250, null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)


class QualityAssurance(models.Model):
    user = models.OneToOneField('SystemUser', on_delete=models.CASCADE)


class Translator(models.Model):
    user = models.OneToOneField('SystemUser', on_delete=models.CASCADE)
