from django.test import TestCase
from .models import AppVote

# Create your tests here.
class Test_AppVote(TestCase):
   
    def setUp(self):
        newapp=AppVote('novel','image.png','author',0.0,0.0,0.0)
        self.assertIsInstance(newapp,AppVote)
    def test_project(self):
        newapp=AppVote(1,'novel','image.png','author',0.0,0.0,0.0)
        newapp.add_project()
        query=AppVote.objects.all()
        self.assertTrue(len(query)==1)
    
        