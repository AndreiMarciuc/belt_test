from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class Quote(models.Model):
    quoted_by = models.CharField(max_length=80)
    message = models.TextField()
    owner = models.ForeignKey(User, related_name='quotes')
    favorited_by= models.ManyToManyField(User,related_name='favorites')