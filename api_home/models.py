from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localdate


class Account(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, unique=True)
    CF_username = models.CharField(blank=False, null=False, max_length=100)
    CF_rating = models.IntegerField(default=0, blank=True)
    SEM_SPI_List = models.JSONField(default=dict, blank=True, null=True)
    created_on = models.DateField(default=localdate)

    def modify_SPI(self, **kwargs):
        for key,value in kwargs:
            self.SEM_SPI_List[key] = value
        self.save()

