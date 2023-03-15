import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')
django.setup()

from http import HTTPStatus
from unittest import TestCase

from django.test import Client
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'SibDoski')

