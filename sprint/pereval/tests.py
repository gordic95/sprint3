from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Pereval, Coords, User
from .serializers import PerevalSerializer


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        user_1 = User.objects.create(name='name', fam='fam', otc='otc', email='email', tel='999999')
        coords_1 = Coords.objects.create(latitude='21.2121', longitude='43.4343', height='800')
        self.pereval_1 = Pereval.objects.create(user=user_1, coords=coords_1, title='sometitle', beautyTitle='somesbeautytitle', other_titles='someothertitle')

    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_detail(self):
        url = reverse('pereval-detail', kwargs={'pk': self.pereval_1.id})
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class PerevalSerializerTestCase(TestCase):
    def test_ok(self):
        user_1 = User.objects.create(name='name1', fam='fam1', otc='otc1', email='test1', tel='111111')
        coords_1 = Coords.objects.create(latitude='33.3333', longitude='44.4444', height='1000')
        self.pereval_1 = Pereval.objects.create(user=user_1, coords=coords_1, title='sometitle', beautyTitle='somebeautytitle', other_titles='someothertitle')

    def test_check(self):
        serializer_data = PerevalSerializer(self.pereval_1).data

        expected_data = [
            {
                'id': 1,
                "user": {
                    "name": "name1",
                    "fam": "fam1",
                    "otc": "otc1",
                    "email": "test1",
                    "tel": "111111"
                },
                "coords": {
                    "id": 1,
                    "latitude": "33.3333",
                    "longitude": "44.4444",
                    "height": "1000",
                },
                "level": None,
                "images": None,
                "title":  "sometitle",
                "beautyTitle": "somebeautytitle",
                "other_titles": "someothertitle",
                "connect":  None,
                "add_time": None,
                "status": None,
            }
        ]

        self.assertEqual(expected_data, serializer_data)

