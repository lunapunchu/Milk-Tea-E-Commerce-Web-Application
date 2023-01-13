from unicodedata import name
from django.db import models

# Create your models here.

class Post_New(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_Discount(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_Milk(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_Soda(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_Smoothies(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_Recommended(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_List(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post_Cart(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.CharField(max_length=20)
    def __str__(self):
        return self.name