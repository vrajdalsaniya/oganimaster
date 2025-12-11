from django.db import models

# Create your models here.

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)

    def __str__(self):
        return self.cname


class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=200)
    
    # Your original fields (kept, not removed)
    pdis = models.TextField()                 # Product short description
    pprice = models.FloatField()              # Product price
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    description = models.TextField()          # Full description
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.pname
