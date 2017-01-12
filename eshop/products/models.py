# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField("Название",max_length=20)
    value = models.IntegerField("Цена")
    desc = models.TextField("Описание")

    class Meta:
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField('Name', max_length=25)
    email = models.EmailField('Email')
    usercom = models.TextField('Comment')
    product = models.ForeignKey(Product)
