from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.feedback import Feedback
from .models.cart import cart
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','phoneno','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminFeedback(admin.ModelAdmin):
    list_display = ['uname','feedback']

class AdminCart(admin.ModelAdmin):
    list_display = ['uname','product','cdate']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Feedback, AdminFeedback)
admin.site.register(cart, AdminCart)