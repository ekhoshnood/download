from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id


class Button(models.Model):
    button = models.CharField(max_length=200)

    def __str__(self):
        return self.button


class Text(models.Model):
    button          = models.ForeignKey(Button, on_delete=models.CASCADE)
    text            = models.TextField(max_length=500)

    def __str__(self):
        return self.text



class SaleType(models.Model):
    # wholesale or retail
    saletype                = models.CharField(max_length=50, null=True)

    is_wholesale = models.BooleanField(default=False)
    is_retail = models.BooleanField(default=False)

    def __str__(self):
        return self.saletype


class Senf(models.Model):
    #shoes, glassess or ...
    senf                = models.CharField(max_length=50, null=True)


    shoes = models.BooleanField(default=False)
    bags = models.BooleanField(default=False)
    women_clothes = models.BooleanField(default=False)
    men_clothes = models.BooleanField(default=False)
    kids_clothes = models.BooleanField(default=False)
    underwear = models.BooleanField(default=False)
    makeup = models.BooleanField(default=False)
    homestuff = models.BooleanField(default=False)
    electric_home = models.BooleanField(default=False)
    glasses = models.BooleanField(default=False)
    electrical = models.BooleanField(default=False)

    def __str__(self):
        return self.senf


# data list model
class Channel(models.Model):
    chat_id                 = models.IntegerField(blank=True, null=True, unique=True)
    admin_id                = models.IntegerField(blank=True, null=True)
    admin_user              = models.CharField(max_length=50, null=True)
    chat_title              = models.CharField(max_length=50, blank=True)
    chat_username           = models.CharField(max_length=50)
    phone                   = models.IntegerField(null=True)
    date_purchased          = models.DateField(auto_now_add=True) # TODO: date field will be added when purchasing with this (datetime.datetime.today().date())
    is_purchased            = models.BooleanField(default=True)
    saletype                = models.ManyToManyField(SaleType)
    senf                    = models.ManyToManyField(Senf)

    def __str__(self):
        return self.chat_username


class Post(models.Model):
    channel                 = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message_id              = models.IntegerField(blank=True, null=True)
    date                    = models.IntegerField(blank=True, null=True)
    text                    = models.TextField(max_length=5000, null=True)
    image                   = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.message_id)

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

