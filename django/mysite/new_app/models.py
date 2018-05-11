from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):

    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
