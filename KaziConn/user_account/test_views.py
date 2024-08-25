from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserAPITests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email='testuser@example.com',
            userName='testuser',
            firstName='Test',
            lastName='User',
            password='testpassword'
        )
        cls.token = RefreshToken.for_user(cls.user)

    def get_auth_header(self):
        return {'HTTP_AUTHORIZATION': f'Bearer {self.token.access_token}'}

    def test_create_user(self):
        url = reverse('user_create')
        data = {
            'email': 'kaziconn@example.com',
            'userName': 'newuser',
            'firstName': 'New',
            'lastName': 'User',
            'password': 'newpassword'
        }
        response = self.client.post(url, data, format='json', **self.get_auth_header())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_list(self):
        url = reverse('user_list')
        response = self.client.get(url, **self.get_auth_header())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        url = reverse('user_update', kwargs={'pk': self.user.id})
        data = {'firstName': 'Updated'}
        response = self.client.patch(url, data, format='json', **self.get_auth_header())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.firstName, 'Updated')

    def test_delete_user(self):
        url = reverse('user_delete', kwargs={'pk': self.user.id})
        response = self.client.delete(url, **self.get_auth_header())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
