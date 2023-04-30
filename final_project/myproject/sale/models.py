from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class Product(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=7,decimal_places=2)
    weight = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField(upload_to='products')
    def __str__(self):
        return "{} {}".format(self.pk, self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    def __str__(self):
        return "{} {}".format(self.pk, self.user)
    
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Order(models.Model):
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE)
    reciept = models.ImageField(upload_to='reciepts')
    def __str__(self):
        return "order: %s"%(self.pk)

class Item(models.Model):
    order = models.ForeignKey( Order, on_delete=models.CASCADE)
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return "order:{} {} of {}".format(self.order, self.quantity, self.product)