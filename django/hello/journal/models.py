from django.db import models


class users(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class trade(models.Model):
    login = models.ForeignKey(users, on_delete=models.CASCADE)
    secure_name = models.CharField(max_length=200)
    price_open = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField('date open')


class trade_close(models.Model):
    open_trade = models.ForeignKey(trade, on_delete=models.CASCADE)
    price_close = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField('date open')
