from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=255)  # blank == true is possible
    phone_number = models.CharField(max_length=255) 
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    detailed_message = models.CharField(max_length=255)
    
    def __str__(self):
        return self.fullname
