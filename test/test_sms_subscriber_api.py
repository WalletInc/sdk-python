# coding: utf-8

"""
    wallet-api

    API

    The version of the OpenAPI document: 2.1.600
    Contact: development@wallet.inc
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wallet.api.sms_subscriber_api import SmsSubscriberApi


class TestSmsSubscriberApi(unittest.TestCase):
    """SmsSubscriberApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SmsSubscriberApi()

    def tearDown(self) -> None:
        pass

    def test_archive_sms_subscriber(self) -> None:
        """Test case for archive_sms_subscriber

        Archive email subscriber
        """
        pass

    def test_create_sms_subscriber(self) -> None:
        """Test case for create_sms_subscriber

        Create email subscriber
        """
        pass

    def test_fetch_all_sms_subscribers(self) -> None:
        """Test case for fetch_all_sms_subscribers

        Fetch all email subscribers
        """
        pass

    def test_restore_sms_subscriber(self) -> None:
        """Test case for restore_sms_subscriber

        Restore email subscriber
        """
        pass

    def test_update_sms_subscriber(self) -> None:
        """Test case for update_sms_subscriber

        Update email subscriber
        """
        pass


if __name__ == '__main__':
    unittest.main()