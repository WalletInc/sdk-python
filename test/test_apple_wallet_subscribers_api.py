"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.514
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import unittest

import wallet
from wallet.api.apple_wallet_subscribers_api import AppleWalletSubscribersApi  # noqa: E501


class TestAppleWalletSubscribersApi(unittest.TestCase):
    """AppleWalletSubscribersApi unit test stubs"""

    def setUp(self):
        self.api = AppleWalletSubscribersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fetch_apple_wallet_subscriber_activity(self):
        """Test case for fetch_apple_wallet_subscriber_activity

        Fetch subscriber activity  # noqa: E501
        """
        pass

    def test_fetch_apple_wallet_subscribers(self):
        """Test case for fetch_apple_wallet_subscribers

        Fetch all subscribers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
