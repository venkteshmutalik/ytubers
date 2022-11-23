from django.db import models

# Create your models here.


class Slider(models.Model):
    headline = models.CharField(max_length=255)  # blank == true is possible
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date= models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.headline

class Team(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fblink = models.CharField(max_length=255)
    instalink = models.CharField(max_length=255)
    ytlink = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.firstname