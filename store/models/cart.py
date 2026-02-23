from django.db import models
class cart(models.Model):
    uname = models.CharField(max_length=50)
    product = models.CharField(max_length=50, default='', blank=True)
    cdate=models.CharField(max_length=20)

    @staticmethod
    def get_all_carts():
        return cart.objects.all()

