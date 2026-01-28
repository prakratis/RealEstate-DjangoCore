from django.db import models
# Create your models here.
class Properties(models.Model):
    PLotSize = models.IntegerField()
    Rate = models.DecimalField(decimal_places=2 , max_digits=10)
    ColonyName = models.CharField(max_length= 100)
    AreaName = models.CharField(max_length= 100)
    City = models.CharField(max_length= 100)
    PinCode = models.CharField(max_length= 100)
    Image = models.ImageField(upload_to='media/')
