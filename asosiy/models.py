from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=35)
    narx = models.PositiveIntegerField()
    litr = models.FloatField()
    batafsil = models.TextField()
    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=75)
    tel = models.CharField(max_length=60)
    manzil = models.CharField(max_length=100)
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=45)
    yosh = models.PositiveSmallIntegerField()
    ish_vaqt = models.CharField(max_length=45)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    kiritilgan_sana = models.DateField()
    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv,on_delete=models.CASCADE)
    sana= models.DateField()
    mijoz= models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    umumiy_narx= models.PositiveIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)



