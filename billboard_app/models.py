# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Messages(models.Model):
    date = models.DateField(u'Day of the event', help_text=u'Day of the event', null=False)
    title = models.CharField(u'title', help_text=u'title',max_length=50, null=False)
    author = models.CharField(u'name', help_text=u'name', max_length=50, null=False)
    msg = models.TextField(u'Textual Notes', help_text=u'Textual Notes', null=False)

    def __str__(self):
        return self.author

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

