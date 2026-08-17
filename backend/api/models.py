from django.db import models
from django.contrib.auth.models import AbstractUser
import os, uuid

def path_cover(_, filename):
    ext = os.path.splitext(filename)
    return f"covers/{uuid.uuid4().hex}{ext}"

class Author(models.Model):
    author=models.CharField(max_length=100)
    s_author=models.CharField(max_length=100)
    birth=models.DateField(null=True,blank=True)
    nacionality=models.CharField(max_length=50, null=True,blank=True)
    biography=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.author} {self.s_author}"

class Publisher(models.Model):
    publisher=models.CharField(max_length=100)
    cnpj=models.CharField(max_length=18,unique=True,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    site=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=255)    
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher=models.ForeignKey(Publisher, on_delete=models.CASCADE)    
    isbn=models.CharField(max_length=255)	            
    description=models.TextField()	                      
    language=models.CharField(max_length=255,default="Português")	   
    year=models.IntegerField()	                  
    pages=models.IntegerField()         	             
    price=models.DecimalField(max_digits=10,decimal_places=2) 	  
    stock=models.IntegerField()	                                  
    discount=models.DecimalField(max_digits=10,decimal_places=2)	   
    available=models.BooleanField(default=True)	               
    dimensions=models.CharField(max_length=255)              
    width=models.DecimalField(max_digits=10,decimal_places=2)       
    cover=models.ImageField(upload_to=path_cover,blank=True,null=True)     

    def __str__(self):
        return self.title
    
class Image(models.Model):
    image=models.ImageField(upload_to="covers")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem #{self.pk}"