# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)  # 使用外键链接过来
    nickname = models.CharField(max_length=10, default='不愿透露身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.message


class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()


class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    restp = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status
