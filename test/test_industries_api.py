"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.514
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import unittest

import wallet
from wallet.api.industries_api import IndustriesApi  # noqa: E501


class TestIndustriesApi(unittest.TestCase):
    """IndustriesApi unit test stubs"""

    def setUp(self):
        self.api = IndustriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fetch_all_industries(self):
        """Test case for fetch_all_industries

        Fetch all industries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
