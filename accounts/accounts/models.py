from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class User_detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Ip_adress(models.Model):
    ip = models.ForeignKey(User_detail, on_delete=models.CASCADE)
    ipadress = models.CharField(max_length=100)

    def __str__(self):
        return str(self.ipadress)




# Create your models here.
class Post_money(models.Model):
    azn1 = models.IntegerField(verbose_name='1.gun qiymet')
    coin1 = models.IntegerField(verbose_name='1.gun Coin')
    
    azn2 = models.IntegerField(verbose_name='2.gun qiymet')
    coin2 = models.IntegerField(verbose_name='2.gun Coin')

    azn3 = models.IntegerField(verbose_name='3.gun qiymet')
    coin3 = models.IntegerField(verbose_name='3.gun Coin')
    
    azn4= models.IntegerField(verbose_name='4.gun qiymet')
    coin4 = models.IntegerField(verbose_name='4.gun Coin')

    azn5 = models.IntegerField(verbose_name='5.gun qiymet')
    coin5 = models.IntegerField(verbose_name='5.gun Coin')
    
    azn6 = models.IntegerField(verbose_name='6.gun qiymet')
    coin6 = models.IntegerField(verbose_name='6.gun Coin')

    azn7 = models.IntegerField(verbose_name='7.gun qiymet')
    coin7 = models.IntegerField(verbose_name='7.gun Coin')
    
    azn8 = models.IntegerField(verbose_name='8.gun qiymet')
    coin8 = models.IntegerField(verbose_name='8.gun Coin')


    azn9 = models.IntegerField(verbose_name='9.gun qiymet')
    coin9 = models.IntegerField(verbose_name='9.gun Coin')
    
    azn10 = models.IntegerField(verbose_name='10.gun qiymet')
    coin10 = models.IntegerField(verbose_name='10.gun Coin')


    azn11 = models.IntegerField(verbose_name='11.gun qiymet')
    coin11 = models.IntegerField(verbose_name='11.gun Coin')
    
    azn12 = models.IntegerField(verbose_name='12.gun qiymet')
    coin12 = models.IntegerField(verbose_name='12.gun Coin')

    azn13 = models.IntegerField(verbose_name='13.gun qiymet')
    coin13 = models.IntegerField(verbose_name='13.gun Coin')
    
    azn14= models.IntegerField(verbose_name='14.gun qiymet')
    coin14 = models.IntegerField(verbose_name='14.gun Coin')

    azn15 = models.IntegerField(verbose_name='15.gun qiymet')
    coin15 = models.IntegerField(verbose_name='15.gun Coin')
    
    azn16 = models.IntegerField(verbose_name='16.gun qiymet')
    coin16 = models.IntegerField(verbose_name='16.gun Coin')

    azn17 = models.IntegerField(verbose_name='17.gun qiymet')
    coin17 = models.IntegerField(verbose_name='17.gun Coin')
    
    azn18 = models.IntegerField(verbose_name='18.gun qiymet')
    coin18 = models.IntegerField(verbose_name='18.gun Coin')


    azn19 = models.IntegerField(verbose_name='19.gun qiymet')
    coin19 = models.IntegerField(verbose_name='19.gun Coin')
    
    azn20 = models.IntegerField(verbose_name='20.gun qiymet')
    coin20 = models.IntegerField(verbose_name='20.gun Coin')

    azn21 = models.IntegerField(verbose_name='21.gun qiymet')
    coin21 = models.IntegerField(verbose_name='21.gun Coin')
    
    azn22 = models.IntegerField(verbose_name='22.gun qiymet')
    coin22 = models.IntegerField(verbose_name='22.gun Coin')

    azn23 = models.IntegerField(verbose_name='23.gun qiymet')
    coin23 = models.IntegerField(verbose_name='23.gun Coin')
    
    azn24= models.IntegerField(verbose_name='24.gun qiymet')
    coin24 = models.IntegerField(verbose_name='24.gun Coin')

    azn25 = models.IntegerField(verbose_name='25.gun qiymet')
    coin25 = models.IntegerField(verbose_name='25.gun Coin')
    
    azn26 = models.IntegerField(verbose_name='26.gun qiymet')
    coin26 = models.IntegerField(verbose_name='26.gun Coin')

    azn27 = models.IntegerField(verbose_name='27.gun qiymet')
    coin27 = models.IntegerField(verbose_name='27.gun Coin')
    
    azn28 = models.IntegerField(verbose_name='28.gun qiymet')
    coin28 = models.IntegerField(verbose_name='28.gun Coin')


    azn29 = models.IntegerField(verbose_name='29.gun qiymet')
    coin29 = models.IntegerField(verbose_name='29.gun Coin')
    
    azn30 = models.IntegerField(verbose_name='30.gun qiymet')
    coin30 = models.IntegerField(verbose_name='30.gun Coin')