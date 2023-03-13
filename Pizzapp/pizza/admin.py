from django.contrib import admin
from .models import Pizza, Category, Order, Extras


admin.site.register(Pizza)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Extras)


# Register your models here.
