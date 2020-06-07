# pages/tests.py 
from django.test import TestCase 
from django.urls import reverse 

class HomepageTests(TestCase): 
    def test_homepage_status_code(self): 
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200) 
        
    def test_homepage_url_name(self): 
        response = self.client.get(reverse('connection')) 
        self.assertEqual(response.status_code, 200)

