from django.db import models
from profile.models import Customer
from service_app.models import Service

# Create your models here.

class Booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    s_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    b_status = models.CharField(max_length=10)
    b_amt = models.IntegerField()
    b_date = models.DateField()

    def __str__(self):
        return f"Booking {self.b_id} - {self.b_status}"