from django.db import models

# Create your models here.
from django.db import models


class Posting(models.Model):
     name = models.CharField(
         max_length=64,
         verbose_name='name',
         help_text='Your name',
     )
     message = models.CharField(
         max_length=255,
         verbose_name='message',
         help_text='please messege',
     )
     created_at = models.DateTimeField(
         auto_now_add=True,
         verbose_name='datedatedate',
     )