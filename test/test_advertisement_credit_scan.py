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
from wallet.model.status import Status
globals()['MerchantID'] = MerchantID
globals()['NanoID'] = NanoID
globals()['Status'] = Status
from wallet.model.advertisement_credit_scan import AdvertisementCreditScan


class TestAdvertisementCreditScan(unittest.TestCase):
    """AdvertisementCreditScan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdvertisementCreditScan(self):
        """Test AdvertisementCreditScan"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AdvertisementCreditScan()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
