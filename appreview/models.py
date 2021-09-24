from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    userPhoto=CloudinaryField('image')
    username=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    contact=PhoneNumberField(null=True)
    location=models.CharField(null=True,blank=True, max_length=30)
    
    @receiver(post_save, sender=User)
    def _post_save_receiver(sender,instance,created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(username=instance)
        
    def __str__(self):
        return f'self.username'
    
class AppVote(models.Model):
    appname=models.CharField(max_length=30,editable=True)
    appimage=CloudinaryField('image')
    author=models.CharField(max_length=30,)
    livelink=models.URLField(null=True, max_length=200)
    design=models.DecimalField(max_digits=2,default=0.0,decimal_places=1,validators=[MaxValueValidator(9.9),MinValueValidator(1)])
    usability=models.DecimalField(max_digits=3,default=0.0,decimal_places=1,validators=[MaxValueValidator(9.9),MinValueValidator(1)])
    content=models.DecimalField(max_digits=3,default=0.0,decimal_places=1,validators=[MaxValueValidator(9.9),MinValueValidator(1)])
    total=models.DecimalField(max_digits=6,decimal_places=4,default=0.0)
    
    
    def add_project(self):
        self.save()
    def delete_app(self):
        self.delete()
    
