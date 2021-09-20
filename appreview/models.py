from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    userPhoto=CloudinaryField('image')
    username=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    
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
    design=models.DecimalField(max_digits=3,default=0.00,decimal_places=2)
    usability=models.DecimalField(max_digits=3,default=0.00,decimal_places=2)
    content=models.DecimalField(max_digits=3,default=0.00,decimal_places=2)
    total=models.DecimalField(max_digits=4,decimal_places=2,default=0.00)
    
    
    def add_project(self):
        self.save()
    
