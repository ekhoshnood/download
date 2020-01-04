from django.db import models

from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


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


# data list model
def upload_location(*args, **kwargs):
    file_path = 'media/text1.jpg'
    return file_path


class Channels(models.Model):
    chat_id                 = models.IntegerField(blank=True, null=True)
    admin_id                = models.IntegerField(blank=True, null=True)
    ad_user                 = models.CharField(max_length=50, blank=True, null=True)
    chat_title              = models.CharField(max_length=50)
    chat_username           = models.CharField(max_length=50)
    message_id              = models.IntegerField(blank=True, null=True)
    date                    = models.IntegerField(blank=True, null=True)
    text                    = models.TextField(max_length=5000)
    image                   = models.ImageField(blank=True, null=True)
    # wholesale or retail
    is_wholesale            = models.BooleanField(default=False)
    is_retail               = models.BooleanField(default=False)
    # JOBS
    shoes                   = models.BooleanField(default=False)
    bags                    = models.BooleanField(default=False)
    women_clothes           = models.BooleanField(default=False)
    men_clothes             = models.BooleanField(default=False)
    kids_clothes            = models.BooleanField(default=False)
    underwear               = models.BooleanField(default=False)
    makeup                  = models.BooleanField(default=False)
    homestuff               = models.BooleanField(default=False)
    electric_home           = models.BooleanField(default=False)
    glasses                 = models.BooleanField(default=False)
    electrical              = models.BooleanField(default=False)

    def __str__(self):
        return self.chat_title


    def get_remote_image(self, image_url):
        print("in def get remote image")
        if self.image_url and not self.image:
            print("after if")
            img_temp = NamedTemporaryFile(delete=True)
            print("before write")
            img_temp.write(urlopen(self.image_url).read())
            print("before flush")
            img_temp.flush()
            print("before save")
            self.image.save(f"image_{self.pk}", File(img_temp))
        print("before final save")
        self.save()
        print("before return")
        return