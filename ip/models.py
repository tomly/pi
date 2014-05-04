from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    time = models.DateTimeField('time updated')
    def __unicode__(self):
        return self.name