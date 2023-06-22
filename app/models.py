from django.db import models


class domain(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
# Create your models here.
class blog(models.Model):
    images= models.ImageField(upload_to='imgs', null=True)
    title= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    type= models.ForeignKey("domain", on_delete=models.CASCADE)
    desc= models.CharField(max_length=500)
    # name= models.CharField(max_length=500)
    schedule_from=models.TimeField( blank=True,null=True)
    schedule_to=models.TimeField( blank=True,null=True)
    Total_Seat=models.IntegerField(default=0,null=True)
    long_desc=models.TextField(default='',null=True)
    name= models.ForeignKey('trainer',on_delete=models.CASCADE)
    # models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class trainer(models.Model):
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='img')
    bio=models.CharField(max_length=100)
    domain=models.ForeignKey("domain", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
class pricing(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    features=models.ManyToManyField('features')

class features(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name