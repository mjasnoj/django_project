# coding=utf-8
# https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/

from django import template

register = template.Library()


@register.filter(name='convert')
def convert(value, rate):
    return str(float(value) * float(rate))