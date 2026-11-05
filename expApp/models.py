from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY_CHOICES = [
    ("food","FOOD"),("bill","BILL"),("fuel","FUEL")
]
PAYMENT_CHOICES=[
    ("upi","UPI"),("card","CARD")
]
class expModel(models.Model):
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField (auto_now_add=True)
    category=models.CharField(default="food",choices=CATEGORY_CHOICES,max_length=10)
    payment=models.CharField(default="upi",choices=PAYMENT_CHOICES,max_length=10)