from django.db import models

# Create your models here.


class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_fullname = models.CharField(max_length=30)
    c_login_id = models.CharField(max_length=30, unique=True)
    c_password = models.CharField(max_length=10)
    c_contact = models.BigIntegerField()
    c_email = models.EmailField(max_length=30)
    c_address = models.CharField(max_length=256)

    def __str__(self):
        return self.c_fullname



class Electrician(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_fullname = models.CharField(max_length=30)
    e_login_id = models.CharField(max_length=30, unique=True)
    e_password = models.CharField(max_length=10)
    e_contact = models.BigIntegerField()
    e_email = models.EmailField(max_length=30)
    e_address = models.CharField(max_length=50)
    e_qualification = models.CharField(max_length=30)

    def __str__(self):
        return str(self.e_id)



