from django.db import models

# Create your models here.
class Person(models.Model):

    MAN = 0
    WOMAN = 1

    HOKKAIDO = 0
    TOHOKU = 5
    TOKYO = 10
    CHIBA = 11
    KANAGAWA = 12
    SAITAMA = 13
    TOCHIGI = 14
    IBARAGI = 15
    CHUBU = 20
    KANSAI = 25
    CHUGOKU = 30
    SHIKOKU = 35
    KYUSHU = 40
    OKINAWA = 45

    name = models.CharField(max_length=128)
    
    birthday = models.DateTimeField()
   
    sex = models.IntegerField(editable=False)
  
    address_from = models.IntegerField()
 
    current_address = models.IntegerField()

    email = models.EmailField()


class Manager(models.Model):


    DEP_ACCOUNTING = 0  
    DEP_SALES = 5  
    DEP_PRODUCTION = 10  
    DEP_DEVELOPMENT = 15
    DEP_HR = 20  
    DEP_FIN = 25
    DEP_AFFAIRS = 30
    DEP_PLANNING = 35
    DEP_BUSINESS = 40
    DEP_DISTR = 45 
    DEP_IS = 50  

    
 #   person = models.ForeignKey('Person')
   
    department = models.IntegerField()
  
    joined_at = models.DateTimeField()
 
    quited_at = models.DateTimeField(null=True, blank=True)


class Worker(models.Model):


#    person = models.ForeignKey('Person')

    joined_at = models.DateTimeField()

    quited_at = models.DateTimeField(null=True, blank=True)

#    manager = models.ForeignKey('Manager')
