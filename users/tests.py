from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru", is_staff=True, is_superuser=True
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        url = reverse("users:users-list")
        data = {"email": "test1@test.ru", "password": "test"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_list_users(self):
        url = reverse("users:users-list")
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["results"][0]["email"],
            "test@test.ru"
        )

    def test_retrieve_users(self):
        url = reverse("users:users-detail", kwargs={"pk": self.user.pk})
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["email"],
            "test@test.ru")

    def test_update_user(self):
        url = reverse(
            "users:users-detail", args=(self.user.pk,))
        data = {"email": "test1@test.ru"}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["email"],
            "test1@test.ru"
        )

    def test_delete_user(self):
        url = reverse("users:users-detail", args=(self.user.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            User.objects.count(),
            0
        )