from django.db import models


class HiddenNumbers(models.Model):
    numbers = models.CharField('числа', max_length=2)

    def __str__(self):
        return self.numbers


class guesswork(models.Model):
    witch_1 = models.CharField('число', max_length=2)
    witch_2 = models.CharField('число', max_length=2)


class PowerOfAttorney(models.Model):
    attorney_1 = models.CharField('доверие-1', max_length=3)
    attorney_2 = models.CharField('доверие-2', max_length=3)