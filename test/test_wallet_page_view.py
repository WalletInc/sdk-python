"""
    wallet-api

    API  # noqa: E501

    The version of the OpenAPI document: 2.1.514
    Contact: development@wallet.inc
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import wallet
from wallet.model.merchant_id import MerchantID
from wallet.model.wt_wallet_page_view_geo_point import WTWalletPageViewGeoPoint
globals()['MerchantID'] = MerchantID
globals()['WTWalletPageViewGeoPoint'] = WTWalletPageViewGeoPoint
from wallet.model.wallet_page_view import WalletPageView


class TestWalletPageView(unittest.TestCase):
    """WalletPageView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWalletPageView(self):
        """Test WalletPageView"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WalletPageView()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
