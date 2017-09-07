# -*- coding: utf-8 -*-
from unittest import TestCase
from deploybot.client import Client
import os


class ClientTest(TestCase):
    # Bootstrap
    def setUp(self):
        TestCase.setUp(self)

        account = os.environ.get('DEPLOYBOT_ACCOUNT')
        token = os.environ.get('DEPLOYBOT_TOKEN')

        self.client = Client(account, token)

    # Tests de default url raises an error without parameters
    def test_get_url_without_parameter(self):
        self.assertRaises(TypeError, self.client.get_url())

    # Tests de default url return a full url
    def test_get_url_with_account_parameter(self):
        result_expected = "https://test.deploybot.com/api/v1/"

        self.assertEqual(result_expected, self.client.get_url("test"))

    # Tests de default url return a full url
    def test_get_url_with_endpoint_parameter(self):
        result_expected = "https://test.deploybot.com/api/v1/deploy"

        self.assertEqual(result_expected, self.client.get_url("test", "deploy"))

    # Test get
    def test_get(self):
        self.assertNotEquals("", self.client.get("users"))

    # Test post
    def test_post(self):
        self.assertNotEquals("", self.client.post("users", {"foo": "bar"}))