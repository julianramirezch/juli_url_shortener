from django.db import models
from django.conf import settings
from .utils import code_generator, create_shortcode
from .validators import validator_dot_com, validate_url
# from django.urls import reverse
from django_hosts.resolvers import reverse
# Create your models here.


SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class JuliURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(JuliURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        """ refresh shorcodes in django shell """
        qs = JuliURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes: {}".format(new_codes)


class JuliURL(models.Model):
    """ Create JuliURL Class """
    url = models.CharField(max_length=220, validators=[validate_url, validator_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = JuliURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(JuliURL, self).save(*args, **kwargs)

    # use the url original name
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        """ reverse url path """
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path
