from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (
    ('computers','computers'),
    ('phones','phones'),
    ('games','games'),
    ('books','books'),
    ('clothes','clothes')
)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200, default='', blank=False)
    description = models.TextField(max_length=2000, default='', blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=False)
    brand = models.CharField(max_length=200, default='', blank=False)
    category = models.CharField(max_length=100,blank=False,choices=CATEGORY_CHOICES)
    ratings = models.DecimalField(max_digits=1,decimal_places=1,default=0,blank=False)
    available_quantity = models.IntegerField(default=1,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    
    
