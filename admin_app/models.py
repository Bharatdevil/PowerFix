from django.db import models

# Create your models here.
class Admin(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_fullname = models.CharField(max_length=30)
    a_login_id = models.CharField(max_length=30, unique=True)
    a_password = models.CharField(max_length=10)
    a_contact = models.BigIntegerField()
    a_email = models.EmailField(max_length=30)
    a_address = models.CharField(max_length=50)

    def __str__(self):
        return self.a_fullname