from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTestCase(TestCase):
    
    def test_user_can_register(self):
        """Test that users can register"""
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        # Check user was created
        self.assertTrue(User.objects.filter(username='testuser').exists())
    
    def test_user_can_login(self):
        """Test that users can log in"""
        # Create a user first
        User.objects.create_user(username='testuser', password='testpass123')
        
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        # Check user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)
    
    def test_user_can_logout(self):
        """Test that users can log out"""
        # Create and login user
        User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        
        # Logout
        response = self.client.get(reverse('logout'))
        
        # Check user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)
# Create your tests here.
