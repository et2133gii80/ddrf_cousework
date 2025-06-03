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

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.id,
                    "time_to_complete": "00:02:00",
                    "periodicity": 1,
                    "habit": "test полезная привычка",
                    "place_of_execution": "test место",
                    "time_execution": "12:00:00",
                    "sign_of_a_pleasant_habit": False,
                    "reward": "test вознаграждение",
                    "published": "Не опубликован",
                    "related_habit": None,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            result
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
        self.assertEqual(
            Habit.objects.count(),
            2)


    def test_retrieve_habit(self):
        url = reverse("habits:habits-detail", kwargs={"pk": self.habit.pk})

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()["habit"],
            "test полезная привычка"
        )

    def test_update_habit(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))

        data = {"habit": "test1 полезная привычка", "reward": "test вознаграждение"}

        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["habit"],
            "test1 полезная привычка",
        )

    def test_delete_habit(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Habit.objects.count(), 0)

    def test_user_habits_list(self):
        url = "/user-habits-list/"

        response = self.client.get(url)

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 7,
                    "time_to_complete": "00:02:00",
                    "periodicity": 1,
                    "habit": "test полезная привычка",
                    "place_of_execution": "test место",
                    "time_execution": "12:00:00",
                    "sign_of_a_pleasant_habit": False,
                    "reward": "test вознаграждение",
                    "published": "Не опубликован",
                    "related_habit": None,
                    "owner": 6,
                }
            ],
        }

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            result
        )
