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
from wallet.model.nano_id import NanoID
globals()['MerchantID'] = MerchantID
globals()['NanoID'] = NanoID
from wallet.model.wallet_configuration import WalletConfiguration


class TestWalletConfiguration(unittest.TestCase):
    """WalletConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWalletConfiguration(self):
        """Test WalletConfiguration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WalletConfiguration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
