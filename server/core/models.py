from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Sales(models.Model):
    file =models.FileField()


class Client(models.Model):
    FullName = models.CharField(max_length=100)
    Wilaya = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=50)
    Function = models.CharField(max_length=50)


class Employee(models.Model):
    FullName = models.CharField(max_length=100)
    Wilaya = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber =models.CharField(max_length=50)
    Function = models.CharField(max_length=50)

class  Values(models.Model):
    id=models.CharField(max_length=6,null=False,blank=False,primary_key=True)
    name=models.CharField(max_length=30,null=False,blank=False)
    ticker=models.CharField(max_length=6,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    start_date=models.DateField(null=False,blank=False)
    end_date=models.DateField(blank=True,max_length=30,null=True)
    sector=models.CharField(max_length=30,null=False,blank=False)
    industry=models.CharField(max_length=30,null=False,blank=False)
    employees_count=models.CharField(blank=True,max_length=30,null=True)
    sic_no=models.CharField(blank=True,max_length=30,null=True)
    location=models.TextField(blank=True,max_length=30,null=True)
    exchange_id=models.CharField(max_length=5,null=False,blank=False)
    cik_no=models.CharField(blank=True,max_length=30,null=True)
    cusip=models.CharField(blank=True,max_length=30,null=True)
    currency_id=models.CharField(max_length=5,null=False,blank=False)
    data_source_id=models.CharField(max_length=5,null=False,blank=False)
    ckr_log=models.CharField(max_length=5,null=False,blank=False)
    similar_fund_log=models.CharField(max_length=5,null=False,blank=False)
    address=models.TextField(max_length=100,null=False,blank=False)
    company_name=models.CharField(max_length=30,null=False,blank=False)
    phone_no=models.CharField(max_length=15,null=False,blank=False)
    website=models.CharField(max_length=30,null=False,blank=False)
    is_Active=models.CharField(max_length=5,null=False,blank=False)
    url_slug=models.CharField(max_length=30,null=False,blank=False)
    delisted_date=models.DateField(blank=True,max_length=30,null=True)
    delisted_reason=models.TextField(blank=True,max_length=30,null=True)
    image_name=models.CharField(blank=True,max_length=30,null=True)
    image_aspect_ratio=models.CharField(max_length=10,null=False,blank=False)
    cumulative_return=models.DateTimeField(max_length=10,null=False,blank=False)

    def _str_(self):
        return self.name

class  Returns(models.Model):
    equity_id=models.AutoField(max_length=6,null=False,blank=False,primary_key=True)
    start_date=models.DateField(null=False,blank=False)
    returns=models.DecimalField(max_digits=20,decimal_places=20,null=False,blank=False)
    equity_id=models.CharField(max_length=6,null=False,blank=False)
    open=models.DecimalField(max_digits=19,decimal_places=10,null=False,blank=False)
    high=models.DecimalField(max_digits=19,decimal_places=10,null=False,blank=False)
    low=models.DecimalField(max_digits=19,decimal_places=10,null=False,blank=False)
    close=models.DecimalField(max_digits=19,decimal_places=10,null=False,blank=False)
    adj_close=models.DecimalField(max_digits=19,decimal_places=10,null=False,blank=False)
    def _str_(self):
        return self.equity_id


