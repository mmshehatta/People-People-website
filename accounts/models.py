from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def uploadProfileImage(instance , filename):
    imageName , extension = filename.split('.')
    return "accounts/%s.%s"%(instance.user , extension)

# ****************** City Model *******************************
class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# ****************** Profile Model *******************************
class Profile(models.Model):
    user = models.OneToOneField(User , related_name='user_peofile' , on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    image = models.ImageField(default='default.jpg',upload_to=uploadProfileImage)
    bio  = models.CharField(max_length=100)
    city = models.ForeignKey(City , related_name='user_city' , on_delete=models.CASCADE,null=True)
    street = models.CharField(max_length=100)
    stat  = models.CharField(max_length=15)
    zipCode = models.CharField(max_length=15)
    website_url = models.URLField(max_length=500)
    def __str__(self):
        return str(self.user)



