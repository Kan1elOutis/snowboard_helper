import os

import django

from products.models import Product

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings')
django.setup()

from http import HTTPStatus
from unittest import TestCase

from django.test import Client
from django.urls import reverse


class ProductsViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'SibDoski - Каталог')
        self.assertEqual(response.context_data['object_list'], products)
