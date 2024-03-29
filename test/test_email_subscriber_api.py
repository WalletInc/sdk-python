"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.535
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import unittest

import wallet
from wallet.api.email_subscriber_api import EmailSubscriberApi  # noqa: E501


class TestEmailSubscriberApi(unittest.TestCase):
    """EmailSubscriberApi unit test stubs"""

    def setUp(self):
        self.api = EmailSubscriberApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_email_subscriber(self):
        """Test case for archive_email_subscriber

        Archive email subscriber  # noqa: E501
        """
        pass

    def test_create_email_subscriber(self):
        """Test case for create_email_subscriber

        Create email subscriber  # noqa: E501
        """
        pass

    def test_fetch_all_email_subscribers(self):
        """Test case for fetch_all_email_subscribers

        Fetch all email subscribers  # noqa: E501
        """
        pass

    def test_restore_email_subscriber(self):
        """Test case for restore_email_subscriber

        Restore email subscriber  # noqa: E501
        """
        pass

    def test_update_email_subscriber(self):
        """Test case for update_email_subscriber

        Update email subscriber  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
