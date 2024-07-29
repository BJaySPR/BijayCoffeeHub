from django.db import models

# Create your models here.
class our_story(models.Model):   
    sub_body = models.TextField()
    main_body = models.TextField()

    def __str__(self):
        return self.sub_body
    
class our_vision(models.Model):
    sub_body = models.TextField()

    def __str__(self):
        return self.sub_body
    
class HotCoffee(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    # discount = models.CharField(max_length=200)
    images = models.ImageField(upload_to='Media')


class ColdCoffee(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    # discount = models.CharField(max_length=200)
    images = models.ImageField(upload_to='Media')

class Offer_Service(models.Model):
    discount_percent = models.IntegerField()
    descriptions = models.CharField(max_length=200)
    offer_starting_time = models.CharField(max_length=200)

    def __str__(self):
        return self.descriptions