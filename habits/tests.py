from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.habit = Habit.objects.create(
            habit="test полезная привычка",
            place_of_execution="test место",
            time_execution="12:00",
            reward="test вознаграждение",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_list_habit(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_create_habit(self):
        url = reverse("habits:habits-list")
        data = {
            "habit": "test1 полезная привычка",
            "reward": "test1 вознаграждение",
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )



    def test_retrieve_habit(self):
        url = reverse("habits:habits-detail", kwargs={"pk": self.habit.pk})

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_update_habit(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))

        data = {"habit": "test1 полезная привычка", "reward": "test вознаграждение"}

        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_delete_habit(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_user_habits_list(self):
        url = "/user-habits-list/"

        response = self.client.get(url)


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
