from django.db import models
from profile.models import Electrician  # Foreignkey of Electrician

class Service(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=20)
    s_description = models.CharField(max_length=100)
    s_price = models.IntegerField()
    e_id = models.ForeignKey(Electrician, on_delete=models.CASCADE,db_column='e_id')

    def __str__(self):
        return self.s_name