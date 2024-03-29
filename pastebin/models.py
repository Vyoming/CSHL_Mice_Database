from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import Activation
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.utils.encoding import smart_text
import datetime
#class User(models.Model):
#    pass

# Create your models here.

class Paste(models.Model):



    CHOICES = (
        ('Black6', 'Black6'),
        ('129S1/SvImJ', '129S1/SvImJ'),
        ('129X1/SvJ', '129X1/SvJ'),
        ('A/J', 'A/J'),
        ('AKR/J', 'AKR/J'),
        ('BALB/cByJ', 'BALB/cByJ'),
        ('BALB/cJ', 'BALB/cJ'),
        ('BTBR T+ Itpr3tf/J', 'BTBR T+ Itpr3tf/J'),
        ('C3H/HeJ', 'C3H/HeJ'),
        ('C57BL/6J', 'C57BL/6J'),
        ('C57BL/6NJ', 'C57BL/6NJ'),
        ('C57BL/10J', 'C57BL/10J'),
        ('CBA/J', 'CBA/J'),
        ('CBA/CaJ', 'CBA/CaJ'),
        ('DBA/1J', 'DBA/1J'),
        ('DBA/2J', 'DBA/2J'),
        ('FVB/NJ', 'FVB/NJ'),
        ('NOD/ShiLtJ', 'NOD/ShiLtJ'),
        ('SJL/J', 'SJL/J'),
        ('TALLYHO/JngJ', 'TALLYHO/JngJ'),
    )
    created_on = models.DateTimeField(auto_now_add=True)

    Age = models.TextField("When was your mice born?", null = True)
    Strain = models.TextField(max_length=1, choices=CHOICES)
    Genotype = models.TextField()

    def contact_default():
        mail = Activation.objects.get()
        return {"email": mail.email}
    Contact = models.CharField("Write your email here", max_length=40, blank=True)

    name = models.CharField(max_length=40, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #AG = Age.date
    #CR = datetime.datetime.now()
    #Ag = TimeDiff(Age,created_on)

    #Ag = Age.second - CR.seconds
    #num_days = Ag / 60 / 60 / 24

    def __unicode__(self):
        return self.name or str(self.id)

    def get_absolute_url(self):
        return ('pastebin_paste_detail', [self.id])
