"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":    
    from douban_client import DoubanClient

    API_KEY = '074b071d3b024f8315e11557b106ee89'
    API_SECRET = '35e9df8c4c8a7435'


    SCOPE = 'shuo_basic_r,shuo_basic_w'
    your_redirect_uri = 'http://hobo.sinaapp.com/'
    client = DoubanClient(API_KEY, API_SECRET, your_redirect_uri, SCOPE)


    print 'Go to the following link in your browser:' 
    print client.authorize_url
    code = raw_input('Enter the verification code:')
    client.auth_with_code(code)

