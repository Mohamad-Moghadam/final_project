
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group
from rest_framework import status
from django.urls import reverse





class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse('create-user')
        data = {
            "username":"testali21",
            "email":"testali21@email.com",
            "password":"testali1122"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], 'testali21')



