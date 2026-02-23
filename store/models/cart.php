from django.db import models
class Product(models.Model):
    uname = models.CharField(max_length=50)
    puname = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    
    @staticmethod
    def get_all_cart():
        return Cart.objects.all()


    