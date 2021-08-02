from django.db import models
# from users.models import User
from django.contrib.auth.models import User
from django.db.models.fields import related
from offers.models import Offer


# Create your models here.

class Need(models.Model):
    # name = models.CharField(max_length=100 , null=False , blank=False , unique=True)
    # id by default exists

    # Relation with users by user_id
    borrower = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)

    # Relation with offers by offer_id
    offer = models.ForeignKey(Offer, related_name="offers", on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.borrower} need to take offer {self.offer}"