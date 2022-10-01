from django.db import models

# Create your models here.
class registerd_user(models.Model):
    first_name = models.CharField(max_length=25,null=False,blank=False)
    last_name = models.CharField(max_length=25,null=False,blank=False)
    email = models.EmailField(null=False,max_length=25,blank=False)
    mobile = models.CharField(max_length=13,blank=False,null=False)
    user_type = models.CharField(max_length=13,blank=False,null=False)
    username = models.CharField(max_length=25,blank=False,null=False)
    password1 = models.CharField(max_length=25,blank=False,null=False)
    password2 = models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.username

class addProduct(models.Model):
    P_name = models.CharField(max_length=25,blank=False,null=False)
    P_code = models.CharField(max_length=25,blank=False,null=False)
    P_category = models.CharField(max_length=25,blank=False,null=False)
    P_price = models.IntegerField()
    P_quantity = models.IntegerField()

    def total(self):
        return self.P_price * self.P_quantity

    def __str__(self):
        return self.P_name

class addReturn(models.Model):
    P_name = models.CharField(max_length=25,blank=False,null=False)
    P_code = models.CharField(max_length=25,blank=False,null=False)
    P_category = models.CharField(max_length=25,blank=False,null=False)
    P_quantity = models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return  self.P_name


class salesAdd(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    price = models.IntegerField()
    qnt = models.IntegerField()

    def totalsale(self):
        return self.price * self.qnt

    def __str__(self):
        return self.name































