import random
import string
from unittest import TestCase

import requests


class ApiTestCase(TestCase):
    def setUp(self) -> None:
        self.client = requests.Session()

    @staticmethod
    def _generate_random_string(length=10, use_numbers=True, use_letters=True):
        chars = ''
        if use_numbers:
            chars = chars + string.digits
        if use_letters:
            chars = chars + string.ascii_uppercase
        return ''.join(random.choices(chars, k=length))

    def url(self, relative):
        return 'http://localhost:8000/' + relative

    def test_create(self):
        description = self._generate_random_string()
        body = {
            'description': description
        }
        result = self.client.post(url=self.url('items'), json=body)
        self.assertEqual(201, result.status_code)
        self.assertEqual({
            'description': description,
            'id': AlwaysTrue(),
            'available_amount': 0
        }, result.json())

    def test_list(self):
        first_description = self._generate_random_string()
        body = {
            'description': first_description
        }
        self.client.post(url=self.url('items'), json=body)

        second_description = self._generate_random_string()
        body = {
            'description': second_description
        }
        self.client.post(url=self.url('items'), json=body)

        params = {
            'amount': 2,
            'order_by': 'id',
            'order': 'DESC'
        }
        result = self.client.get(url=self.url('items'), params=params)
        self.assertEqual(200, result.status_code)
        self.assertEqual([{
            'description': second_description,
            'id': AlwaysTrue(),
            'available_amount': 0
        }, {
            'description': first_description,
            'id': AlwaysTrue(),
            'available_amount': 0
        }], result.json())

    def test_get(self):
        description = self._generate_random_string()
        body = {
            'description': description
        }
        result = self.client.post(url=self.url('items'), json=body)
        self.assertEqual(201, result.status_code)
        item_id = result.json()['id']

        result = self.client.get(url=self.url('items/{}'.format(item_id)))
        self.assertEqual(200, result.status_code)
        self.assertEqual({
            'description': description,
            'id': item_id,
            'available_amount': 0
        }, result.json())

        result = self.client.get(url=self.url('items/{}'.format(random.randint(1, 100000000))))
        self.assertEqual(404, result.status_code)
        self.assertEqual({'error_code': 'ITEM_NOT_FOUND'}, result.json())

    def test_update(self):
        description = self._generate_random_string()
        body = {
            'description': description
        }
        result = self.client.post(url=self.url('items'), json=body)
        self.assertEqual(201, result.status_code)
        item_id = result.json()['id']

        result = self.client.get(url=self.url('items/{}'.format(item_id)))
        self.assertEqual(200, result.status_code)
        self.assertEqual({
            'description': description,
            'id': item_id,
            'available_amount': 0
        }, result.json())

        body = {
            'increment': True
        }
        result = self.client.put(url=self.url('items/{}'.format(item_id)), json=body)
        self.assertEqual(200, result.status_code)

        result = self.client.get(url=self.url('items/{}'.format(item_id)))
        self.assertEqual(200, result.status_code)
        self.assertEqual({
            'description': description,
            'id': item_id,
            'available_amount': 1
        }, result.json())


class AlwaysTrue(object):
    def __eq__(self, other):
        return other is not None
