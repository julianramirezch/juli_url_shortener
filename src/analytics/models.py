from django.db import models

# Create your models here.
from shortener.models import JuliURL


class ClickEventManager(models.Manager):
    """ Return how many clicks has every link """
    def create_event(self, juli_instance):
        if isinstance(juli_instance, JuliURL):
            obj, created = self.get_or_create(juli_url=juli_instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    juli_url    = models.OneToOneField(JuliURL, on_delete=models.PROTECT)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{i}'.format(i=self.count)
