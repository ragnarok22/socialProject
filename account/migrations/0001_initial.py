# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('about_me', models.TextField()),
                ('sign', models.CharField(max_length=100)),
                ('born_date', models.DateField()),
                ('sex', models.CharField(max_length=1, default='U', choices=[('M', 'Masculino'), ('W', 'Femenino'), ('U', 'Sin definir')])),
                ('civil_status', models.CharField(max_length=1, default='S', choices=[('M', 'casado'), ('S', 'soltero'), ('F', 'con novia'), ('C', 'es complicado')])),
                ('is_conected', models.BooleanField(default=False)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
                'verbose_name': 'Perfil',
            },
        ),
    ]
