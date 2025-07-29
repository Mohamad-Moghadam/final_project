
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import token_blacklist
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

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







class DetailAccountViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='strongpassword123'
        )


        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.url = reverse('user-detail-account') 

    def test_authenticated_user_can_see_own_account(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)

    def test_unauthenticated_user_cannot_access_account_detail(self):
        self.client.credentials() 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)





class EditAccountViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='strongpassword123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.url = reverse('account-edit')

    def test_authenticated_user_can_edit_own_account(self):
        data = {
            'username': 'updateduser',
            'email': 'updated@example.com'
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_unauthenticated_user_cannot_edit_account(self):
        self.client.credentials()  
        data = {
            'username': 'hackeruser',
        }
        response = self.client.put(self.url, data)
