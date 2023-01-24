import unittest
from unittest.mock import Mock
from importlib import import_module
from inspect import getmembers
import os
import yaml

from google.ads.googleads import client as Client
mock_credentials_instance = Mock()

class GoogleAdsMockTest(TestCase):
      def _create_test_client(self, **kwargs):
        with Mock.patch.object(
            Client.oauth2,
            "get_installed_app_credentials",
            return_value=mock_credentials_instance,
        ):
            result = Client.GoogleAdsClient._get_client_kwargs(config)
            self.assertEqual(
                result,
                {
                    "credentials": mock_credentials_instance,
                    "developer_token": self.developer_token,
                    "use_proto_plus": self.use_proto_plus,
                    "endpoint": None,
                    "login_customer_id": None,
                    "logging_config": None,
                    "linked_customer_id": None,
                    "http_proxy": None,
                },
            )
