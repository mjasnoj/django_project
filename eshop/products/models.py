# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class OnlyAvailable(models.Manager):
    def get_queryset(self):
        return super(OnlyAvailable, self).get_queryset().filter(is_available=True)

    def set_all_available(self):
        Product.objects.update(is_available=True)


class Product(models.Model):
    name = models.CharField("Название", max_length=20)
    value = models.IntegerField("Цена")
    desc = models.TextField("Описание")
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = OnlyAvailable()

    class Meta:
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return self.name

    def set_available(self, f):
        pass


class Comment(models.Model):
    name = models.CharField('Name', max_length=25)
    email = models.EmailField('Email')
    usercom = models.TextField('Comment')
    product = models.ForeignKey(Product)

