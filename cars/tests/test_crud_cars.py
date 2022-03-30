import json

from rest_framework.test import APITestCase

from cars.models import Car
from cars.serializers import CarSerializer


class TestCrudCars(APITestCase):

    def setUp(self):
        self.client.post(
            "/api/cars/",
            {
                "color": "silver",
                "name": "mazda"
            }
        )

    def test_get_cars(self):
        result = self.client.get(
        )
        assert result.json()[0] == {
            "id": 1,
            "color": "silver",
            "name": "mazda"
        }

    def test_get_unique_car(self):
        result = self.client.get(
            "/api/cars/1/"
        )
        assert result.json() == {
            "id": 1,
            "color": "silver",
            "name": "mazda"
        }

    def test_delete_unique_car(self):
        result = self.client.delete(
            "/api/cars/1/"
        )
        assert result.status_code == 204

    def test_update_unique_car(self):
        result = self.client.put(
            "/api/cars/1/",
            {"id": 1,
             "name": "BMW",
             "color": "white"
             }
        )
        assert result.json() == {
            "name": "BMW",
            "color": "white",
            "id": 1
        }
