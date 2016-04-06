from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    about_me = models.TextField()
    sign = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name='profile')
    born_date = models.DateField()
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('W', 'Femenino'),
        ('U', 'Sin definir'),
    )
    CIVIL_STATUS_CHOICES = (
        ('M', 'casado'),
        ('S', 'soltero'),
        ('F', 'con novia'),
        ('C', 'es complicado'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='U')
    civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS_CHOICES, default='S')
    is_conected = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def age(self):
        actual = timezone.now().year
        born_year = self.born_date.year
        return actual - born_year

    def __str__(self):
        return self.user.username
