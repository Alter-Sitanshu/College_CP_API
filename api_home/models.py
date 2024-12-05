from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Account(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    CF_username = models.CharField(blank=False, null=False, max_length=100)
    CF_rating = models.IntegerField(default=0, blank=True)
    SEM_SPI_List = models.JSONField(default=dict, blank=True)
    created_on = models.DateField(default=now)

    def modify_SPI(self, **kwargs):
        for key,value in kwargs:
            self.SEM_SPI_List[key] = value
        self.save()

