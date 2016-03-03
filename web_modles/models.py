# coding=utf-8
from django.db import models

# Create your models here.


class Agent(models.Model):
    hostname = models.CharField(null=True, blank=True, max_length=256)
    is_pem = models.BooleanField(default=False)
    join_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.hostname


class Url(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    url = models.CharField(null=True, blank=True, max_length=256)
    source_ip = models.GenericIPAddressField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Record(models.Model):
    url = models.ForeignKey(Url)
    agent = models.ForeignKey(Agent)
    code = models.IntegerField(default=0)
    source_code = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
