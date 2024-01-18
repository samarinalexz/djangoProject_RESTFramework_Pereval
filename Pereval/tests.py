from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Pereval.models import PerevalAdded, Coords, User, Level, Image
from Pereval.serializers import PerevalSerializer, UserSerializer, CoordinateSerializer, LevelSerializer, \
    PerevalListSerializer


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval1 = PerevalAdded.objects.create(
            title='Перевал 1',
            beauty_title='второе название1',
            other_title='другое1',
            connect='соединяет1',
            coord=Coords.objects.create(
                latitude=1.1,
                longitude=1.1,
                height=1.1,
            ),
            user=User.objects.create(
                surname='Петров',
                name='Петр',
                otc='Павлович',
                email='petrov@mail.com',
                phone='89101234567',
            ),
            level=Level.objects.create(
                    winter='1a',
                    summer='1a',
                    autumn='1a',
                    spring='1a',
                ),
        )

        self.pereval2 = PerevalAdded.objects.create(
            title='Перевал 2',
            beauty_title='второе название2',
            other_title='другое2',
            connect='соединяет2',
            coord=Coords.objects.create(
                latitude=2.2,
                longitude=2.2,
                height=2.2,
            ),
            user=User.objects.create(
                surname='Андропов',
                name='Александр',
                otc='Алексеевич',
                email='andropov@mail.com',
                phone='89201234567',
            ),
            level=Level.objects.create(
                winter='2a',
                summer='2a',
                autumn='2a',
                spring='2a',
                ),
        )

    def test_get_perevals(self):
        response = self.client.get('/perevals/')
        serializer_list_pereval = PerevalSerializer([self.pereval1, self.pereval2], many=True).data
        self.assertEqual(serializer_list_pereval, response.data)
        self.assertEqual(len(serializer_list_pereval), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_pereval_edit_by_id(self):
        response = self.client.get(reverse('pereval_update-detail', kwargs={'pk': self.pereval1.id}))
        serializer_data = PerevalSerializer(self.pereval1).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_get_user_by_email(self):
        email = self.pereval1.user.email
        url = f'/perevals/?user__email={email}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
