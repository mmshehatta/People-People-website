from django.db import models
from django.utils.text import slugify


from django.contrib.auth.models import User
from datetime import datetime



class Category(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False , unique=True)
    def __str__(self):
        return self.name




class Offer(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False , unique=False)
    # slug = models.SlugField(unique=True,null=True,blank=True )
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='media' ,null=True , blank=True)
    place = models.CharField(max_length=100 , null=False , blank=False , unique=False)
    # log = models.DecimalField(max_digits=9, decimal_places=6)
    # lat = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField(default=datetime.now, blank=True)
    # phone = PhoneField(blank=True)
    phone = models.CharField(max_length=11, blank=True)

    offer_statts=(
        ('available','available'),
        ('borrowered','borrowered'),
    )
    status = models.CharField(max_length=10, choices=offer_statts ,default='available')
    # user_relation
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Categories_Relation
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __unicode__(self):
    #      return self.name

    # def save(self , *args , **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)


    def __str__(self):
        return self.name
