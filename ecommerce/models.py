from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('S' ,'Shirt'),
    ('SW' ,'Sport Wear'),
    ('OW' ,'Outwear'),
)

LABEL_CHOICES = (
    ('P' ,'primary'),
    ('S' ,'secondary'),
    ('D' ,'danger'),
)


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=2)
    label = models.CharField(choices=LABEL_CHOICES , max_length=1)
    def __str__(self):
        return self.title
    

class OrderItem(models.Model):
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    def __str__(self):
        return self.item

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(Item)
    start_date = models.DateTimeField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username