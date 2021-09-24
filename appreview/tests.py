from django.test import TestCase
from .models import AppVote, Profile

# Create your tests here.
class Test_AppVote(TestCase):
   
    def setUp(self):
        newapp=AppVote('novel','image.png','author',0.0,0.0,0.0)
        self.assertIsInstance(newapp,AppVote)
    
    def test_add_project(self):
        newapp=AppVote(1,'novel','image.png','author',0.0,0.0,0.0)
        newapp.add_project()
        query=AppVote.objects.all()
        self.assertTrue(len(query)==1)
        newapp.delete_app()
        
    def delete_test(self):
         newapp=AppVote(2,'novel1','image1.png','author1',0.0,0.0,0.0)
         newapp.add_project()
         newapp.delete_app()
         query=AppVote.objects.filter(appimage='image1.png')
         self.assertTrue(len(query)==0)
         
class Test_Profile(TestCase):
    def setUp(self):
        newprofile=Profile('download.png',1,'enthuist','+254700000000','Nairobi') 
        self.assertIsInstance(newprofile,Profile)
         
        
    
    
        