"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.514
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import unittest

import wallet
from wallet.api.utilities_api import UtilitiesApi  # noqa: E501


class TestUtilitiesApi(unittest.TestCase):
    """UtilitiesApi unit test stubs"""

    def setUp(self):
        self.api = UtilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_payment_prefixes(self):
        """Test case for get_payment_prefixes

        Get payment prefixes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
