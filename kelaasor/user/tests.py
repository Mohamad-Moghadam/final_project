
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import token_blacklist



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




class LogoutUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="logoutuser", 
            password="strongpassword12", 
            email="logoutuser2@email.com"
        )

        self.refresh=RefreshToken.for_user(self.user)
        self.access_token=str(self.refresh.access_token)
        self.refresh_token=str(self.refresh)
        self.url=reverse("user-logout")


    def test_user_can_logout(self):
        data = {"refresh_token":self.refresh_token}
        response = self.client.post(self.url, data, format="json")    

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["detail"], "User Logged Out Successfully")


