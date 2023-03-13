from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, db_index=True, editable=False)

    def __str__(self) -> str:
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Pizza(models.Model):
    name = models.CharField(max_length= 200, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    favorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='Pizza')
    def __str__(self):
        return self.name
    
class Extras(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= "customer_order")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_order")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=True)
    extra = models.ManyToManyField(Extras,blank=True)
    size = models.CharField(choices=[ ('small', 'Small'),('medium', 'Medium'),('large', 'large')], max_length=6, default='medium')
    total_price = models.PositiveIntegerField(default=0)
    def __str__(self) -> str:
        return "".join(str(self.id)+'_'+self.customer.username +"_"+self.pizza.name)


    